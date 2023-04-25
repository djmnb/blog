---
title: spring系列学习
data: 2023-4-20
---





### 配置文件

Spring Boot中的配置文件是用于配置应用程序的属性和参数的文件。Spring Boot支持多种类型的配置文件，包括属性文件、**YAML文件**、JSON文件等. 配置文件可以包含应用程序的所有配置参数，例如数据库连接信息、日志配置、服务器端口等。这些参数可以通过@ConfigurationProperties注解和@Value注解在应用程序中访问。

Spring Boot 提供了许多有用的特性，以简化配置文件的使用。以下是一些配置文件中的特殊用法：

#### 配置文件的多环境支持：

Spring Boot 支持使用不同的配置文件来区分不同的环境（如开发、测试和生产环境）。您可以在 `application.yml` 或 `application.properties` 文件中使用 `spring.profiles.active` 属性来激活特定的环境配置文件。例如，在 `application.yml` 文件中：

```yaml
spring:
  profiles:
    active: dev
```

这将激活名为 `application-dev.yml` 的配置文件。您还可以通过命令行参数或环境变量来覆盖此属性。

#### 配置文件中的占位符

您可以在配置文件中使用 `${...}` 占位符引用其他属性。例如：

```properties
app.message=Hello, Spring Boot!
app.greeting=${app.message} Welcome to our application!
```

在这个例子中，`app.greeting` 的值将包含 `app.message` 的值。

#### 配置文件的优先级

Spring Boot 允许您将配置文件放在不同的位置，如项目的根目录、`config/` 目录、类路径等。不同位置的配置文件具有不同的优先级。例如，项目根目录下的 `application.properties` 文件的优先级高于类路径下的 `application.properties` 文件。这意味着在多个位置定义相同的属性时，具有较高优先级的配置文件中的值将覆盖较低优先级的配置文件中的值。

#### 使用 YAML 配置文件中的锚点和别名

在 YAML 格式的配置文件中，您可以使用锚点（`&`）和别名（`*`）来避免重复。例如：

```yaml
app:
  dataSource:
    default: &default
      driverClassName: org.h2.Driver
      url: jdbc:h2:mem:testdb
      username: sa
      password: password
    primary: *default
    secondary:
      <<: *default
      url: jdbc:h2:mem:anotherdb
```

在这个例子中，我们使用了锚点和别名来避免重复定义 `default` 数据源的属性。

#### 获取pom.xml的环境变量

在配置文件中使用"@@"通常是指使用**Maven资源过滤器**，用于将Maven构建过程中的**项目属性值替换到配置文件中**。

在Maven中，可以使用"@变量名@"的形式来引用项目属性，例如"@artifactId@"引用项目的artifactId值，"@version@"引用项目的版本号等等。除了这些内置的变量之外，还可以在pom.xml文件中定义自己的属性，并在配置文件中使用"@@自定义变量名@@"的形式来引用它们。

例如，在pom.xml文件中定义了一个自定义属性my-property：

```xml
<properties>
  <my-property>hello world</my-property>
</properties>
```

然后在配置文件中使用"@@"引用它：

```properties
my.property.value=@my-property@
```

在Maven构建过程中，Maven会自动将"@@"语法替换成对应的属性值，因此上面的配置文件将被替换成：

```properties
my.property.value=hello world
```

需要注意的是，在配置文件中使用"@@"时，变量名需要与pom.xml文件中定义的属性名保持一致，否则无法正确地替换属性值。



### 配置文件读取

在 Spring Boot 中，常用的配置文件格式有两种：`.properties` 和 `.yml`（或 `.yaml`）。Spring Boot 自动加载项目根目录下的 `application.properties` 或 `application.yml` 文件作为默认的配置文件。您可以使用以下方式来读取配置文件中的值：

#### 使用 `@Value` 注解

在需要注入配置值的地方，使用 `@Value` 注解并指定配置的键。例如，假设 `application.properties` 文件中有一个属性 `app.message`：

```properties
app.message=Hello, Spring Boot!
```

您可以使用 `@Value` 注解将该属性值注入到一个变量中：

```java
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class AppConfig {

    @Value("${app.message}")
    private String message;

    public String getMessage() {
        return message;
    }
}
```

#### 使用 `@ConfigurationProperties` 注解

为了更方便地管理和验证配置，您可以使用 `@ConfigurationProperties` 注解将配置文件中的属性值绑定到一个 Java 对象上。首先，创建一个带有 `@ConfigurationProperties` 注解的类，并为该类的字段添加 getter 和 setter 方法：

```java
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Component
@ConfigurationProperties(prefix = "app")
public class AppConfig {

    private String message;

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
```

在这个示例中，`prefix = "app"` 表示将配置文件中以 `app` 为前缀的属性绑定到 `AppConfig` 类的字段上。

#### 使用 `Environment` 对象

在 Spring 中，您还可以使用 `Environment` 对象来访问配置文件中的属性值。首先，将 `Environment` 注入到您的组件中：

```java
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Component;

@Component
public class AppConfig {

    private final Environment env;

    public AppConfig(Environment env) {
        this.env = env;
    }

    public String getMessage() {
        return env.getProperty("app.message");
    }
}
```

这种方法适用于在运行时动态访问配置值的情况。

这些方法可以应用于不同的配置文件格式（`.properties` 或 `.yml`）。您可以根据实际需求和偏好选择合适的方式来读取配置文件中的值。



### 过滤器

下面是定义过滤器的几种方式



#### FilterRegistrationBean

在 Spring Boot 中，你可以通过实现 `javax.servlet.Filter` 接口并注册一个 `Filter` Bean 来创建一个过滤器。下面是创建一个简单过滤器的步骤：

1. 首先，创建一个 Java 类，实现 `javax.servlet.Filter` 接口。在这个类中，你需要实现 `init`、`doFilter` 和 `destroy` 方法。

```java
import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.IOException;

public class MyFilter implements Filter {

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // 初始化操作，例如加载配置、设置参数等
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        // 在此处执行过滤逻辑，例如请求头检查、权限验证等
        // ...

        // 如果符合过滤条件，继续执行后续过滤器和请求处理
        chain.doFilter(request, response);
    }

    @Override
    public void destroy() {
        // 清理操作，例如释放资源、清理缓存等
    }
}
```

2. 然后，将创建的过滤器类注册为 Spring Bean 并配置过滤器顺序。你可以通过创建一个 `FilterRegistrationBean` Bean 来实现这一点。

```java
import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class FilterConfig {

    @Bean
    public FilterRegistrationBean<MyFilter> myFilterRegistration() {
        FilterRegistrationBean<MyFilter> registration = new FilterRegistrationBean<>();
        registration.setFilter(new MyFilter());
        registration.addUrlPatterns("/*"); // 设置过滤器拦截的 URL 模式
        registration.setOrder(1); // 设置过滤器的执行顺序
        return registration;
    }
}
```

在这个示例中，我们创建了一个名为 `MyFilter` 的过滤器，并通过 `FilterConfig` 类将其注册为一个 Spring Bean。`MyFilter` 会拦截所有的 URL（通过 `addUrlPatterns("/*")` 配置），并设置其执行顺序为 1（通过 `setOrder(1)` 配置）。

现在，每当有请求到达应用时，`MyFilter` 都会在请求进入控制器之前执行。你可以在 `doFilter` 方法中实现你的过滤逻辑，例如权限检查、日志记录等。

#### @Component` 和 `@Order 注解

在过滤器类上添加 `@Component` 和 `@Order` 注解，将过滤器作为 Spring Bean 进行注册，同时指定执行顺序。这种方式适用于需要 Spring 执行自动扫描的情况。

```java
import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.IOException;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

@Component
@Order(1)
public class MyFilter implements Filter {

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // 初始化操作，例如加载配置、设置参数等
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        // 在此处执行过滤逻辑，例如请求头检查、权限验证等
        // ...

        // 如果符合过滤条件，继续执行后续过滤器和请求处理
        chain.doFilter(request, response);
    }

    @Override
    public void destroy() {
        // 清理操作，例如释放资源、清理缓存等
    }
}
```

#### 使用 `@WebFilter` 注解：

在过滤器类上添加 `@WebFilter` 注解，指定要拦截的 URL 模式。同时，需要在启动类上添加 `@ServletComponentScan` 注解以启用自动扫描。这种方式主要用于 Servlet 容器的过滤器，而不是 Spring 的过滤器，因此在过滤器中无法自动注入其他 Spring Bean。

```java
import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.IOException;

@WebFilter(urlPatterns = "/*", filterName = "myFilter")
public class MyFilter implements Filter {

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // 初始化操作，例如加载配置、设置参数等
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        // 在此处执行过滤逻辑，例如请求头检查、权限验证等
        // ...

        // 如果符合过滤条件，继续执行后续过滤器和请求处理
        chain.doFilter(request, response);
    }

    @Override
    public void destroy() {
        // 清理操作，例如释放资源、清理缓存等
    }
}
```

启动类添加 `@ServletComponentScan` 注解：

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.ServletComponentScan;

@SpringBootApplication
@ServletComponentScan
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```





### 权限校验的几种方式

#### 过滤器



#### 拦截器



#### AOP + RestControllerAdvice

AOP

```java
package com.example.project.AOP;


import com.example.project.excption.LoginError;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;

import javax.servlet.http.HttpServletRequest;

/**
 * 检查用户是否登录
 */
@Aspect
@Component
public class LoginCheck {

    @Around("@annotation(com.example.project.annotation.LoginCheckAnnotation)")  // 只对需要校验的方法进行检查
    public Object checkLogin(ProceedingJoinPoint pjp) throws Throwable {
        HttpServletRequest request = ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest();  // 拿到request对象
        Object userinfo = request.getSession().getAttribute("userinfo");
        if(userinfo == null){
            throw new LoginError("用户未登录");
        }
        return pjp.proceed();
    }

}
```

RestControllerAdvice里面去检测这个异常就可以了



### 请求响应流程

1. 接收请求：客户端（如浏览器或其他应用）向服务器发起 HTTP 请求。请求首先到达服务器上的 Web 服务器，例如 Tomcat、Jetty 或 Undertow。
2. 过滤器（Filter）链：在请求到达 Spring Boot 应用之前，它会经过一系列的过滤器。这些过滤器可以用于处理跨域请求、安全性、编码等问题。过滤器按照定义的顺序依次执行。
3. 请求进入 Spring DispatcherServlet：在过滤器链处理完成后，请求进入 Spring 的核心 Servlet，即 DispatcherServlet。DispatcherServlet 负责将请求路由到合适的控制器（Controller）方法。
4. 解析请求映射：DispatcherServlet 查找与请求 URL 匹配的控制器方法。这是通过处理器映射（HandlerMapping）完成的，它会根据请求的 URL、HTTP 方法和其他条件找到匹配的控制器方法。
5. 参数解析与数据绑定：在找到匹配的控制器方法后，Spring 会解析请求参数并将其绑定到方法参数上。这是通过参数解析器（ArgumentResolver）完成的。参数解析器可以处理各种类型的参数，例如路径参数、查询参数、请求体等。
6. 参数校验：根据需要，Spring 可以对请求参数进行校验。例如，可以使用 JSR-303/JSR-380 校验注解（如 `@NotNull`、`@Size` 等）对请求参数进行校验。
7. 执行控制器方法：参数解析和校验完成后，Spring 会调用匹配的控制器方法并传入解析后的参数。在控制器方法中，可以处理业务逻辑并返回响应数据。
8. AOP 切面：在执行控制器方法时，可以使用 AOP 为目标方法添加切面。切面可以包含前置通知（Before Advice）、后置通知（After Advice）、环绕通知（Around Advice）等，用于实现日志记录、权限控制等功能。
9. 返回值处理：控制器方法执行完成后，Spring 会处理其返回值。返回值处理器（ReturnValueHandler）负责将返回值转换为最终的 HTTP 响应。例如，可以使用 `@ResponseBody` 注解将返回值序列化为 JSON，或者返回一个视图名称（如 "index"）以渲染 HTML 页面。
10. 异常处理：在请求处理过程中，可能会抛出异常。这时，可以使用 `@ControllerAdvice` 或 AOP 的 `@Around` 通知来捕获和处理异常。异常处理方法可以根据异常类型返回不同的错误响应。
11. 视图解析与渲染：如果控制器方法返回的是一个视图名称（例如 "index"），Spring 会使用视图解析器（ViewResolver）来找到与视图名称匹配的视图模板（如 Thymeleaf、Freemarker、JSP 等）。然后，视图模板将使用控制器方法返回的数据渲染 HTML 页面。
12. 生成 HTTP 响应：经过视图渲染或返回值处理后，Spring 会将结果封装成一个 HTTP 响应。响应包括 HTTP 状态码、响应头和响应体。响应体可能包含 JSON 数据、HTML 页面等。
13. 响应过滤器链：在发送响应给客户端之前，响应会经过一系列的过滤器。这些过滤器可以用于处理响应头、响应体等。与请求过滤器链类似，响应过滤器链中的过滤器按照定义的顺序依次执行。
14. 发送响应：最后，Web 服务器将 HTTP 响应发送回客户端。客户端收到响应后可以解析响应数据并采取相应的操作。



### 自定义404处理

#### 方法一

在Spring Boot中，如果你想在@ControllerAdvice类中捕获404异常（Not Found异常），你需要实现`ErrorController`接口并重写`getErrorPath`方法。这样，你可以在@ControllerAdvice类中处理404异常。

首先，创建一个类实现`ErrorController`接口：

```java
import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CustomErrorController implements ErrorController {

    @RequestMapping("/error")
    public ResponseEntity<?> handleError(HttpServletRequest request) {
        Integer statusCode = (Integer) request.getAttribute("javax.servlet.error.status_code");
        if (statusCode == HttpStatus.NOT_FOUND.value()) {
            throw new NotFoundException("资源未找到");
        }
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("内部服务器错误");
    }

    @Override
    public String getErrorPath() {
        return "/error";
    }
}
```

然后，在你的@ControllerAdvice类中处理`NotFoundException`：

```java
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.servlet.ModelAndView;

@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(NotFoundException.class)
    public ModelAndView handleNotFoundException(NotFoundException ex) {
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("error", ex.getMessage());
        modelAndView.setViewName("error/404");
        return modelAndView;
    }

    // 其他异常处理方法...
}
```

这样，当发生404异常时，将会触发`NotFoundException`，然后在`GlobalExceptionHandler`类中处理该异常。

#### 方式二

除了上述方法外，还有一种简单的方法可以在 `@ControllerAdvice` 类中捕获404异常，那就是通过捕获 `NoHandlerFoundException`。首先，你需要在 `application.properties` 或 `application.yml` 文件中启用此功能。

在 `application.properties` 中添加以下内容：

```properties
spring.mvc.throw-exception-if-no-handler-found=true
spring.resources.add-mappings=false
```

或者在 `application.yml` 中添加以下内容：

```yaml
spring:
  mvc:
    throw-exception-if-no-handler-found: true
  resources:
    add-mappings: false
```

这样，Spring Boot会将404视为一个异常，并抛出`NoHandlerFoundException`。现在，在你的 `@ControllerAdvice` 类中处理这个异常：

```java
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.NoHandlerFoundException;

@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(NoHandlerFoundException.class)
    public ModelAndView handleNoHandlerFoundException(NoHandlerFoundException ex) {
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("error", "资源未找到");
        modelAndView.setViewName("error/404");
        return modelAndView;
    }

    // 其他异常处理方法...
}
```

现在，当发生404异常时，`NoHandlerFoundException` 会被捕获并在 `GlobalExceptionHandler` 类中处理。这种方法相对简单，不需要实现 `ErrorController` 接口。

在Spring Boot中，将 `spring.resources.add-mappings` 设置为 `false` 是为了禁用默认的静态资源处理。当你使用 `spring.mvc.throw-exception-if-no-handler-found=true` 配置选项启用 `NoHandlerFoundException` 时，这一设置可以确保404异常被正确处理。

Spring Boot默认配置了静态资源处理，如CSS、JS、图片等。如果没有禁用静态资源处理，当访问一个不存在的静态资源时，Spring Boot将不会抛出 `NoHandlerFoundException`，而是直接返回404状态码。这意味着你的 `@ControllerAdvice` 类将无法捕获到404异常。

通过将 `spring.resources.add-mappings` 设置为 `false`，你可以关闭默认的静态资源处理。这样，无论是访问不存在的静态资源还是其他类型的资源，Spring Boot都会抛出 `NoHandlerFoundException`，使得你的 `@ControllerAdvice` 类能够捕获到所有的404异常。需要注意的是，**禁用默认的静态资源处理后，你需要自己配置静态资源处理规则。**

如果你的应用程序没有使用静态资源，或者已经配置了自定义的静态资源处理规则，那么直接禁用默认的静态资源处理不会有任何问题。如果你需要使用默认的静态资源处理规则，可以考虑使用我在之前回答中提到的实现 `ErrorController` 接口的方法来捕获404异常。



### springmvc中的异常类



#### HttpMessageNotReadableException

在 Spring Boot 应用程序中，HttpMessageNotReadableException 异常通常代表请求的消息无法读取或解析。这个异常通常是由于以下原因之一导致的：

1. 请求的 Content-Type 不正确：如果请求的 Content-Type 不正确，例如请求头中的 Content-Type 是 application/json，但请求体中的数据格式不是 JSON 格式，则会导致 HttpMessageNotReadableException 异常。
2. 请求体中的数据格式不正确：如果请求体中的数据格式不正确，例如请求体中的 JSON 数据格式不符合要求，或者请求体中缺少必要的属性等，也会导致 HttpMessageNotReadableException 异常。
3. 请求体中的数据长度不正确：如果请求体中的数据长度超出了服务器预期的范围，也可能导致 HttpMessageNotReadableException 异常。

当发生 HttpMessageNotReadableException 异常时，Spring Boot 会自动返回一个 HTTP 400 Bad Request 响应，提示客户端请求的消息无法读取或解析。





## 实用功能

### actuator

用来检测项目运行状况

搭配spring-boot-admin **来可视化的监控** spring-boot 程序的运行状态

### Mybatis-Plus

#### 导入依赖

```
<dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
            <version>3.5.3.1</version>
        </dependency>
```

#### 配置数据源

```
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mybatis?useUnicode=true&characterEncoding=utf-8&useSSL=false
    username: root
    password: root
    driver-class-name: com.mysql.cj.jdbc.Driver
```



#### 命名规则

在 MyBatis-Plus 中，数据库表名、字段名和 Java 对象名（实体类名）及其属性名之间的映射关系通常遵循以下规则：

1. 数据库表名与实体类名：
   - 数据库表名通常使用下划线命名法，例如 `user_info`。
   - Java 实体类名应使用驼峰命名法（Pascal Case），例如 `UserInfo`。
   - 如果数据库表名与实体类名不匹配，可以使用 `@TableName` 注解指定实体类对应的数据库表名，例如 `@TableName("user_info")`。
2. 数据库字段名与实体类属性名：
   - 数据库字段名通常使用下划线命名法，例如 `first_name`。
   - Java 实体类属性名应使用小驼峰命名法（Camel Case），例如 `firstName`。
   - 如果数据库字段名与实体类属性名不匹配，可以使用 `@TableField` 注解指定属性对应的数据库字段名，例如 `@TableField("first_name")`。

在 MyBatis-Plus 的默认配置下，框架会自动将下划线命名法的数据库表名和字段名映射到驼峰命名法的实体类名和属性名。因此，只要遵循这些命名规则，通常不需要额外的注解来指定映射关系。

当然，如果您的项目有特殊的命名规则，您可以根据实际需求调整这些映射关系。使用 `@TableName` 和 `@TableField` 注解可以灵活地定制实体类与数据库表之间的映射关系。

> 一定要注意Mybatis-Plus和springboot版本的关系,切记切记

#### 属性名字或者类名与关键字冲突

使用TableName 和 TableField

```
@Data
@TableName("message")  // 指定表名字
public class Message {
    @TableId(type = IdType.AUTO)  // 自增
    private long id;
    @TableField("`like`")
    private int like;  // 这里与关键字冲突,用双引号加反引号
    private String text;
    private long carId;
    private long userId;
}

```

> 尽量不要跟关键字冲突



#### 代码生成

导入依赖

```
 <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-generator</artifactId>
            <version>3.4.1</version>
        </dependency>
```



编写代码

```java
package com.example;

import com.baomidou.mybatisplus.generator.AutoGenerator;
import com.baomidou.mybatisplus.generator.config.DataSourceConfig;
import com.baomidou.mybatisplus.generator.config.GlobalConfig;
import com.baomidou.mybatisplus.generator.config.PackageConfig;
import com.baomidou.mybatisplus.generator.config.StrategyConfig;
import com.baomidou.mybatisplus.generator.config.rules.NamingStrategy;

public class test {

    public static void main(String[] args) {
        // 1. 创建 AutoGenerator 对象
        AutoGenerator generator = new AutoGenerator();

        // 2. 配置数据源
        DataSourceConfig dataSourceConfig = new DataSourceConfig();
        dataSourceConfig.setUrl("jdbc:mysql://localhost:3306/test");
        dataSourceConfig.setDriverName("com.mysql.cj.jdbc.Driver");
        dataSourceConfig.setUsername("root");
        dataSourceConfig.setPassword("mysql666.");
        generator.setDataSource(dataSourceConfig);

        // 3. 配置全局策略
        GlobalConfig globalConfig = new GlobalConfig();
        globalConfig.setOutputDir(System.getProperty("user.dir") + "/src/main/java");
        globalConfig.setAuthor("Your Name");
        globalConfig.setOpen(false);
        generator.setGlobalConfig(globalConfig);

        // 4. 配置包信息
        PackageConfig packageConfig = new PackageConfig();
        packageConfig.setParent("com.example");
        packageConfig.setModuleName("test1");
        generator.setPackageInfo(packageConfig);

        // 5. 配置生成策略
        StrategyConfig strategyConfig = new StrategyConfig();
        strategyConfig.setNaming(NamingStrategy.underline_to_camel);
        strategyConfig.setColumnNaming(NamingStrategy.underline_to_camel);
        strategyConfig.setEntityLombokModel(true);
        strategyConfig.setRestControllerStyle(true);
        strategyConfig.setInclude("car_info","message","order","user"); // 要生成的表名
        generator.setStrategy(strategyConfig);

        // 6. 执行生成
        generator.execute();
    }
}



```

执行一遍即可

**他就会帮我们生成好实体类与mapper还是service,还有controller**



### jwt认证

JWT是指JSON Web Token（JSON网络令牌），是一种用于在网络应用之间传递信息的开放标准（RFC 7519）。它可以作为一种轻量级的安全性传输方式，用于在发送方和接收方之间传递声明。这些声明可以被验证和信任，因此可以用来实现单点登录、用户认证等功能。

JWT由三部分组成，分别是头部（Header）、载荷（Payload）和签名（Signature）。头部包含关于JWT的元数据，如加密算法和类型。载荷包含声明，即要传输的信息，例如用户的ID、过期时间等。签名则是用于验证消息的完整性和认证信息发送方的值。

JWT具有无状态、可扩展、易于传输等特点，因此广泛应用于Web应用程序、移动应用程序和IoT设备等场景。

下面是生成 JWT 的详细流程：

1. 创建 header（头部）：JWT 的 header 包含两部分：token 类型（typ）和使用的哈希算法（alg）。通常，header 是一个 JSON 对象，例如：
   ```
   {
     "alg": "HS256",
     "typ": "JWT"
   }
   ```
   其中，alg 指定了用于签名的算法，常见的有 HS256、HS384、HS512、RS256 等。typ 用于声明数据结构类型，这里是 JWT。

2. 创建 payload（负载）：payload 包含实际需要传递的数据。它通常是一个 JSON 对象，可以包含多个键值对。这些键值对被称为 claims（声明）。有三种类型的 claims：registered（注册）、public（公共）和 private（私有）声明。示例：
   ```
   {
     "sub": "1234567890",
     "name": "John Doe",
     "iat": 1516239022
   }
   ```
   其中，sub 是主题，name 是用户名称，iat 是 token 发布时间。

3. **对 header 和 payload 进行 Base64Url 编码**：将 header 和 payload 分别进行 Base64Url 编码。Base64Url 是一种对 URL 安全的编码方式。编码后的 header 和 payload 称为 JWT 的第一部分和第二部分。

   > 这个Base64Url 编码只是对数据进行了格式化,并没有加密,所以客户端是可以通过这两个东西拿到数据的

4. 连接编码后的 header 和 payload：将编码后的 header 和 payload 用英文句号（.）连接起来，形成一个字符串，如下所示：
   ```
   base64UrlEncodedHeader.base64UrlEncodedPayload
   ```

5. 生成签名：使用指定的哈希算法（如 HS256）对连接后的字符串进行哈希计算，同时用一个密钥（secret）对哈希值进行签名。这将生成一个签名，确保 JWT 在传输过程中没有被篡改。

   > 这里才是加密过程

6. 连接签名：将签名进行 Base64Url 编码后，再与前面生成的字符串用英文句号（.）连接，得到完整的 JWT：
   ```
   base64UrlEncodedHeader.base64UrlEncodedPayload.base64UrlEncodedSignature
   ```
   这个 JWT 可以在需要的场景下传递给其他服务进行认证和授权。

在生成 JWT 后，接收方可以对其进行解码和验证。验证的过程包括解码 header 和 payload，然后使用相同的哈希算法和密钥重新生成签名，如果新生成的签名与接收到的 JWT 中的签名相同，则说明该 JWT 是有效且未被篡改的。

> 在认证的过程中,我们只需要进行同样的前五步,得到前面然后和token的前面进行对比,如果相同就认证成功,不同就说明比篡改了



## 好用的工具类

### jackson

Jackson是一个Java语言的JSON库，用于在Java对象和JSON数据之间进行转换。它可以将Java对象序列化为JSON字符串，也可以将JSON字符串反序列化为Java对象。Jackson可以处理任意复杂度的Java对象，包括对象的继承关系、嵌套关系、集合和映射等。同时，Jackson还支持各种常见的JSON数据格式，包括JSON对象、JSON数组、JSON字符串、JSON数值、JSON布尔值和JSON null值等。

Jackson是一个功能强大、高效稳定的JSON库，在Java开发中被广泛使用。Jackson的主要优点包括：

1. 速度快：Jackson采用了高效的JSON处理算法，可以快速地将Java对象序列化为JSON字符串或者将JSON字符串反序列化为Java对象。
2. 易于使用：Jackson提供了简单易用的API，开发者可以快速地上手并进行相关操作。
3. 可扩展性强：Jackson提供了丰富的注解和接口，可以方便地扩展和定制自己的序列化和反序列化处理逻辑。
4. 配置灵活：Jackson支持各种配置选项，可以控制序列化和反序列化的行为，满足不同应用场景的需求。
5. 开源免费：Jackson是一款开源的JSON库，可以免费使用，并且有一个活跃的社区在维护和更新它的功能。

#### 导入依赖

```xml
<dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-core</artifactId>
            <version>2.13.0</version>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>2.13.0</version>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-annotations</artifactId>
            <version>2.13.0</version>
        </dependency>
```

> 当然springboot已经帮我们导入好了

#### 常用方法

Jackson提供了很多实用的方法，以下是一些常用的方法：

1. `ObjectMapper.writeValueAsString(Object obj)`

该方法将Java对象序列化为JSON字符串，并返回字符串表示。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
Person person = new Person("张三", 25);
String json = objectMapper.writeValueAsString(person);
System.out.println(json); // 输出：{"name":"张三","age":25}
```

2. `ObjectMapper.writeValue(File file, Object obj)`

该方法将Java对象序列化为JSON字符串，并将结果写入指定的文件。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
Person person = new Person("张三", 25);
File file = new File("person.json");
objectMapper.writeValue(file, person);
```

3. `ObjectMapper.readValue(String json, Class<T> valueType)`

该方法将JSON字符串反序列化为Java对象，并返回Java对象的实例。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
String json = "{\"name\":\"张三\",\"age\":25}";
Person person = objectMapper.readValue(json, Person.class);
System.out.println(person.getName()); // 输出：张三
```

4. `ObjectMapper.readValue(File file, Class<T> valueType)`

该方法将JSON文件反序列化为Java对象，并返回Java对象的实例。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
File file = new File("person.json");
Person person = objectMapper.readValue(file, Person.class);
```

5. `JsonNode.get(String fieldName)`

该方法获取JSON节点中指定字段名对应的节点。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
String json = "{\"name\":\"张三\",\"age\":25}";
JsonNode jsonNode = objectMapper.readTree(json);
String name = jsonNode.get("name").asText();
int age = jsonNode.get("age").asInt();
```

6. `JsonNode.iterator()`

该方法返回JSON节点的所有子节点的迭代器。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
String json = "{\"name\":\"张三\",\"friends\":[{\"name\":\"李四\",\"age\":28},{\"name\":\"王五\",\"age\":30}]}";
JsonNode jsonNode = objectMapper.readTree(json);
Iterator<JsonNode> iterator = jsonNode.get("friends").iterator();
while (iterator.hasNext()) {
    JsonNode friend = iterator.next();
    String name = friend.get("name").asText();
    int age = friend.get("age").asInt();
}
```

7. `JsonNode.isArray()`

该方法判断JSON节点是否为数组类型。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
String json = "{\"name\":\"张三\",\"friends\":[{\"name\":\"李四\",\"age\":28},{\"name\":\"王五\",\"age\":30}]}";
JsonNode jsonNode = objectMapper.readTree(json);
if (jsonNode.get("friends").isArray()) {
    // ...
}
```

8. `JsonNode.isObject()`

该方法判断JSON节点是否为对象类型。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
String json = "{\"name\":\"张三\",\"friends\":[{\"name\":\"李四\",\"age\":28},{\"name\":\"王五\",\"age\":30}]}";
JsonNode jsonNode = objectMapper.readTree(json);
if (jsonNode.isObject()) {
    // ...
}
```

9. `ObjectNode.put(String fieldName, JsonNode value)`

该方法向JSON对象节点中添加一个字段，并设置字段值。例如

```java
ObjectMapper objectMapper = new ObjectMapper();
ObjectNode objectNode = objectMapper.createObjectNode();
objectNode.put("name", "张三");
objectNode.put("age", 25);
JsonNode friendsNode = objectMapper.createArrayNode()
        .add(objectMapper.createObjectNode().put("name", "李四").put("age", 28))
        .add(objectMapper.createObjectNode().put("name", "王五").put("age", 30));
objectNode.set("friends", friendsNode);
```

10. `ArrayNode.add(JsonNode value)`

该方法向JSON数组节点中添加一个子节点。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
ArrayNode arrayNode = objectMapper.createArrayNode();
arrayNode.add(objectMapper.createObjectNode().put("name", "李四").put("age", 28));
arrayNode.add(objectMapper.createObjectNode().put("name", "王五").put("age", 30));
```

以上是Jackson库中一些常用的方法，可以满足大部分的需求。当然，Jackson还提供了很多其他的方法，开发者可以根据自己的需要进行查阅和使用。

#### 常用注解

Jackson提供了许多注解，用于控制Java对象和JSON数据之间的转换。以下是一些常用的Jackson注解：

1. `@JsonAnyGetter`和`@JsonAnySetter`

**`@JsonAnyGetter`和`@JsonAnySetter`注解可以用于处理一些未知的属性**。`@JsonAnyGetter`注解标注在任意属性的获取方法上，`@JsonAnySetter`注解标注在任意属性的设置方法上。使用这两个注解可以让Jackson在序列化和反序列化时忽略一些不确定的属性。

2. `@JsonProperty`

`@JsonProperty`**注解可以用于指定Java对象字段和JSON属性之间的映射关系**。可以在Java对象字段上使用`@JsonProperty`注解指定JSON属性的名称，例如：

```java
public class Person {
    @JsonProperty("fullName")
    private String name;
    private int age;
    // ...
}
```

在这个例子中，`@JsonProperty("fullName")`注解将Java对象字段`name`与JSON属性`fullName`建立了映射关系。在将Java对象序列化为JSON字符串或者将JSON字符串反序列化为Java对象时，Jackson都会使用这个映射关系来确定Java对象字段和JSON属性之间的对应关系。

3. `@JsonIgnore`

`@JsonIgnore`注解可以用于标注Java对象字段，**指定在序列化和反序列化时忽略该字段**。例如：

```java
public class Person {
    private String name;
    @JsonIgnore
    private int age;
    // ...
}
```

在这个例子中，`@JsonIgnore`注解标注在Java对象字段`age`上，表示在将Java对象序列化为JSON字符串或者将JSON字符串反序列化为Java对象时，忽略`age`字段。

4. `@JsonFormat`

`@JsonFormat`**注解可以用于指定Java对象字段的日期格式和时区**。例如：

```java
public class Person {
    private String name;
    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", timezone = "GMT+8")
    private Date birthDate;
    // ...
}
```

在这个例子中，`@JsonFormat`注解指定了Java对象字段`birthDate`的日期格式为`yyyy-MM-dd HH:mm:ss`，时区为`GMT+8`。在将Java对象序列化为JSON字符串或者将JSON字符串反序列化为Java对象时，Jackson会根据这个注解来进行日期格式和时区的转换。

5. `@JsonInclude`

`@JsonInclude`**注解可以用于指定在序列化时忽略为空的Java对象字段**。例如：

```java
public class Person {
    private String name;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private Integer age;
    // ...
}
```

在这个例子中，`@JsonInclude`注解指定了Java对象字段`age`在序列化时不包括空值。也就是说，如果`age`字段为`null`，在将Java对象序列化为JSON字符串时，Jackson会忽略这个字段。

除了上面介绍的注解



### Hutool

一个Java基础工具类，对文件、流、加密解密、转码、正则、线程、XML等JDK方法进行封装，组成各种Util工具类，同时提供以下组件：

| 模块               | 介绍                                                         |
| ------------------ | ------------------------------------------------------------ |
| hutool-aop         | JDK动态代理封装，提供非IOC下的切面支持                       |
| hutool-bloomFilter | 布隆过滤，提供一些Hash算法的布隆过滤                         |
| hutool-cache       | 简单缓存实现                                                 |
| hutool-core        | 核心，包括Bean操作、日期、各种Util等                         |
| hutool-cron        | 定时任务模块，提供类Crontab表达式的定时任务                  |
| hutool-crypto      | 加密解密模块，提供对称、非对称和摘要算法封装                 |
| hutool-db          | JDBC封装后的数据操作，基于ActiveRecord思想                   |
| hutool-dfa         | 基于DFA模型的多关键字查找                                    |
| hutool-extra       | 扩展模块，对第三方封装（模板引擎、邮件、Servlet、二维码、Emoji、FTP、分词等） |
| hutool-http        | 基于HttpUrlConnection的Http客户端封装                        |
| hutool-log         | 自动识别日志实现的日志门面                                   |
| hutool-script      | 脚本执行封装，例如Javascript                                 |
| hutool-setting     | 功能更强大的Setting配置文件和Properties封装                  |
| hutool-system      | 系统参数调用封装（JVM信息等）                                |
| hutool-json        | JSON实现                                                     |
| hutool-captcha     | 图片验证码实现                                               |
| hutool-poi         | 针对POI中Excel和Word的封装                                   |
| hutool-socket      | 基于Java的NIO和AIO的Socket封装                               |
| hutool-jwt         | JSON Web Token (JWT)封装实现                                 |

可以根据需求对每个模块单独引入，也可以通过引入`hutool-all`方式引入所有模块。

```
<dependency>
    <groupId>cn.hutool</groupId>
    <artifactId>hutool-all</artifactId>
    <version>5.8.18</version>
</dependency>
```

按需引入

```
<dependency>
    <groupId>cn.hutool</groupId>
    <artifactId>hutool-core</artifactId>
    <version>5.8.18</version>
</dependency>
```

