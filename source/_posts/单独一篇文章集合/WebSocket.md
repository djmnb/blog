---
title: websocket基本使用
date: 2023-4-30
---



# 导入依赖

```
<dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-websocket</artifactId>
        </dependency>
```



# 原生

## 前端

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebSocket Example</title>
</head>

<body>
    <input type="text" id="message" placeholder="Type your message here...">
    <button id="sendBtn">Send</button>
    <div id="output"></div>

    <script>
        const messageInput = document.getElementById("message");
        const sendBtn = document.getElementById("sendBtn");
        const output = document.getElementById("output");

        const socket = new WebSocket("ws://localhost:8080/chat-websocket");

        // 连接打开时触发
        socket.addEventListener("open", (event) => {
            output.innerHTML += "WebSocket connection opened.<br>";
        });

        // 接收到服务器消息时触发
        socket.addEventListener("message", (event) => {
            output.innerHTML += "Server: " + event.data + "<br>";
        });

        // 连接关闭时触发
        socket.addEventListener("close", (event) => {
            output.innerHTML += "WebSocket connection closed.<br>";
        });

        // 发送消息到服务器
        sendBtn.addEventListener("click", () => {
            const message = messageInput.value;
            if (message !== "") {
                socket.send(message);
                messageInput.value = "";
            }
        });

    </script>
</body>

</html>
```

## 后端

### 配置类

```java
@Configuration
public class WebSocketConfig {
    @Bean
    public ServerEndpointExporter serverEndpointExporter(){
        return new ServerEndpointExporter();
    }
}
```

### 通信类

```
@ServerEndpoint(value = "/chat-websocket")
@Component
public class ChatController {
 
    {
        System.out.println("ChatController created");
    }

    @PreDestroy
    public void preDestroy() {
        System.out.println("ChatController preDestroy");
    }

    @RequestMapping("/onlineCount")
    public String onlineCount() {
        return "onlineCount";
    }


    @OnOpen
    public void onOpen(Session session) {
        System.out.println("New connection: " + session.getId());
    }

    @OnMessage
    public void onMessage(String message, Session session) {
        System.out.println("Received message: " + message + " from: " + session.getId());
        try {
            session.getBasicRemote().sendText("Received message: " + message);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @OnError
    public void onError(Throwable error, Session session) {
        System.out.println("Error: " + error.getMessage());
    }

    @OnClose
    public void onClose(Session session) {
        System.out.println("Connection closed: " + session.getId());
    }
}

```



# STOMP 协议



## 订阅与发布

### 前端

```html
<!DOCTYPE html>
<html>
<head>
    <title>Chat Example</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/sockjs-client/1.5.2/sockjs.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/stomp.js/2.3.3/stomp.min.js"></script>
</head>
<body>
<div>
    <input type="text" id="from" placeholder="Your name">
    <input type="text" id="to" placeholder="Recipient">
    <input type="text" id="message" placeholder="Message">
    <button onclick="sendMessage()">Send</button>
</div>
<ul id="chat">
</ul>

<script>
    // 连接WebSocket服务器
    const socket = new SockJS("http://localhost:8080/chat-websocket");
    const stompClient = Stomp.over(socket);

    stompClient.connect({}, function (frame) {
        console.log("Connected: " + frame);
        // 订阅/topic/messages以接收聊天消息
        stompClient.subscribe("/topic/messages", function (response) {
            const message = JSON.parse(response.body);
            showMessage(message);
        });
    });

    function sendMessage() {
        const from = document.getElementById("from").value;
        const to = document.getElementById("to").value;
        const content = document.getElementById("message").value;

        // 发送聊天消息到/app/sendMessage
        stompClient.send("/app/sendMessage", {}, JSON.stringify({
            from: from,
            to: to,
            content: content
        }));
    }

    function showMessage(message) {
        const chat = document.getElementById("chat");
        const li = document.createElement("li");
        li.appendChild(document.createTextNode(message.from + " to " + message.to + ": " + message.content));
        chat.appendChild(li);
    }
</script>
</body>
</html>

```



### 后端

#### 配置类

```java
@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {

    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic");
        config.setApplicationDestinationPrefixes("/app");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/chat-websocket").setAllowedOriginPatterns("*").withSockJS();
    }
}

```

`WebSocketMessageBrokerConfigurer`中的`configureMessageBroker`方法用于配置消息代理相关选项。`MessageBrokerRegistry`对象提供了一些方法，用于自定义消息代理的行为。下面是关于这两个方法的详细解释：

1. `config.enableSimpleBroker("/topic")`：**启用简单消息代理，并指定代理应该处理的目标前缀**。在这个例子中，我们指定了前缀`/topic`。简单消息代理是一个内置的、轻量级的消息代理，适用于简单的用例。当**客户端订阅以`/topic`开头的目标时**，它们会收到发送到这些目标的消息。例如，**如果客户端订阅了`/topic/chat`，那么它们将接收到发送到`/topic/chat`的所有消息。**

2. `config.setApplicationDestinationPrefixes("/app")`：设置应用程序的目标前缀。这个前缀用于定义应用程序特定的消息处理方法。在这个例子中，**我们使用了前缀`/app`。当客户端向以`/app`开头的目标发送消息时**，这些消息将被路由到Spring应用程序中相应的`@MessageMapping`注解的方法。例如，**如果客户端发送了一个目标为`/app/sendMessage`的消息，Spring将查找一个`@MessageMapping("/sendMessage")`注解的方法来处理该消息。**

除了上述方法，`MessageBrokerRegistry`还提供了其他一些方法，用于配置消息代理。这里有一些常用的方法：

- `config.setUserDestinationPrefix(String userDestinationPrefix)`：设置用户目标前缀。这个前缀用于定义用户特定的消息目标。当客户端订阅以该前缀开头的目标时，它们将只收到发送到这些目标的针对特定用户的消息。例如，如果客户端订阅了`/user/queue/notifications`，那么它们将只接收到发送给当前用户的通知消息。

- `config.enableStompBrokerRelay(String... destinationPrefixes)`：启用STOMP代理中继，以便将消息代理的职责委托给外部STOMP代理（如RabbitMQ或ActiveMQ）。这个方法接受一个或多个目标前缀，指定外部代理应处理哪些目标。这对于更复杂的用例和更高的可扩展性非常有用。

这些配置方法用于控制WebSocket消息的路由和处理。您可以根据应用程序的需求选择合适的方法来自定义消息代理行为。



`registerStompEndpoints`方法用于注册WebSocket端点，客户端将通过这些端点与服务器建立WebSocket连接。`StompEndpointRegistry`对象提供了一些方法，用于自定义端点的行为。以下是关于这个方法的详细解释：

- `registry.addEndpoint("/chat-websocket")`：向注册表添加一个新的WebSocket端点，并设置端点的URL路径。在这个例子中，我们使用了路径`/chat-websocket`。客户端将使用此路径与服务器建立WebSocket连接。

在添加端点后，可以使用链式调用来配置端点的其他选项：

- `setAllowedOriginPatterns("*")`：设置允许连接到WebSocket端点的源（即客户端的域）。在这个例子中，我们使用了`"*"`，意味着允许任何域连接到这个端点。您可以通过指定一个或多个特定的域来限制允许连接的来源，以提高安全性。
- `withSockJS()`：启用SockJS支持。SockJS是一个JavaScript库，**用于在不支持原生WebSocket的浏览器中提供类似于WebSocket的功能。通过在服务器端配置中启用SockJS，您可以确保即使在不支持WebSocket的浏览器中，您的应用程序也能够正常工作。**

> 如果启用了了sockjs,那么前端就需要使用sockjs库,如果没有启用就用原生的websocket就可以了

这些方法和选项允许您自定义WebSocket端点的行为，以满足应用程序的需求。您可以根据需要添加和配置多个端点，以支持不同的客户端连接和使用场景。



虽然SockJS和STOMP通常一起使用，以确保在不支持原生WebSocket的浏览器中仍能正常工作，但并非所有情况下都需要同时使用它们。在某些情况下，您可能只需要STOMP，而不需要SockJS，或者只需要原生的WebSocket。

将`withSockJS()`作为一个可选配置项，而不是内置到STOMP配置中，可以为开发人员提供更大的灵活性。这样，您可以根据实际需求和目标浏览器的支持来选择是否启用SockJS。此外，这也有助于确保在不需要SockJS时，应用程序不会因为不必要的额外开销而受到影响。

在实际开发中，如果您打算使用STOMP协议，而且希望确保在各种浏览器环境中都能正常工作，那么开启`withSockJS()`是一个很好的做法。但是，这个决策仍然取决于您的实际需求和场景。

#### 控制层

```java
import com.example.demo.bean.TestBean;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Controller;

@Controller
public class ChatController {

    @Autowired
    private TestBean testBean;

    @Autowired
    private SimpMessagingTemplate messagingTemplate;

    @MessageMapping("/sendMessage")
    @SendTo("/topic/messages")
    public String handleMessage(String message) {
        System.out.println("收到消息: " + message);
        return message;
    }
}
```



## 点对点