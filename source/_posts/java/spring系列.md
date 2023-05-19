---
title: spring系列学习
data: 2023-4-28
tags:	
  - java
  - spring
  - 需要复习
categories:
  - 框架学习
---

# 前言

> 源码看了又看,忘了又忘,还不如多学学怎么用吧

## 全家桶

Spring 全家桶（Spring Ecosystem）包括许多项目和模块，以支持各种应用程序开发需求。以下是 Spring 全家桶中的一些主要项目：

1. Spring Framework：核心框架，提供了依赖注入（DI）、面向切面编程（AOP）、事件处理等基本功能。

2. Spring Boot：简化 Spring 应用程序开发的框架，提供了自动配置、内嵌容器、快速创建微服务等特性。

3. Spring Cloud：基于 Spring Boot 的微服务框架，提供了服务发现、配置中心、断路器等分布式系统开发组件。

4. Spring Data：提供了统一的数据访问层解决方案，包括对关系型数据库、NoSQL 数据库和其他数据存储技术的支持。

5. Spring Security：提供了强大的安全解决方案，支持认证、授权、攻击防护等功能。

6. Spring Integration：提供了企业集成模式的实现，用于集成不同系统和服务。

7. Spring Batch：用于创建高性能批处理应用程序，支持任务调度、分块处理等功能。

8. Spring Web MVC：用于构建基于 Servlet API 的 Web 应用程序，支持 RESTful API、表单处理、文件上传等功能。

9. Spring WebFlux：用于构建响应式 Web 应用程序，支持非阻塞 I/O、异步处理等功能。

10. Spring WebSocket：提供了 WebSocket 通信支持，用于构建实时 Web 应用程序。

11. Spring AMQP：提供了对高级消息队列协议（AMQP）的支持，用于实现消息队列通信。

12. Spring Cloud Stream：基于 Spring Boot 的消息队列框架，提供了对多种消息中间件的抽象和统一接口。

13. Spring Cloud Data Flow：用于构建数据集成和实时数据处理管道的微服务框架。

14. Spring Cloud Gateway：基于 Spring Boot 的 API 网关，提供了路由、过滤、限流等功能。

15. Spring Cloud Function：提供了将 Spring Boot 应用程序作为函数进行部署的支持，用于无服务器计算场景。

以上只是 Spring 全家桶中的部分项目。随着社区的不断发展，Spring 生态系统不断扩展，为开发者提供了丰富的工具和组件。更多关于 Spring 项目的详细信息，可以访问 Spring 官方网站：https://spring.io/projects

> 后面的代码都是基于springboot, 但是很多东西都是spring框架的核心概念

# spring

## 什么是spring

Spring Framework 是一个开源的 Java 应用框架，由 Rod Johnson 创立于 2003 年。它旨在简化企业级 Java 开发，提供了一套完整的解决方案，用于创建各种类型的 Java 应用程序，包括 Web、桌面和分布式应用。Spring Framework 的主要特性如下：

1. Inversion of Control（IoC，控制反转）：Spring Framework 提供了一个 IoC 容器，负责管理对象之间的依赖关系。通过使用控制反转，开发者可以将关注点集中在业务逻辑上，而不是依赖关系的管理和实例化过程。
2. Dependency Injection（DI，依赖注入）：依赖注入是实现 IoC 的一种方法。Spring Framework 支持构造器注入和属性注入，使得对象之间的依赖关系可以在配置文件或注解中声明，从而提高代码的可测试性和可维护性。
3. Aspect-Oriented Programming（AOP，面向切面编程）：Spring Framework 提供了 AOP 支持，允许开发者将横切关注点（如日志记录、事务管理等）从核心业务逻辑中分离出来。这有助于提高代码的模块化程度和可读性。





## 注册bean

在Spring Boot中，有多种方式注册Bean（组件），每种方式都有其使用方法、注意事项、优缺点。以下是主要的注册方式：

### 1. 使用@Component、@Service、@Repository和@Controller注解：

使用方法：将这些注解添加到类上，以便让Spring将其作为组件（Bean）自动注册到上下文中。每个注解都具有特定的用途和语义，但它们都是@Component注解的特殊化版本。

注意事项：确保这些类在组件扫描的路径下，否则Spring将无法自动检测和注册这些组件。

优点：简单易用，易于理解。

缺点：使用注解，与Spring框架产生了耦合。

### 2. 使用@Configuration和@Bean注解：

使用方法：使用@Configuration注解标记配置类，而@Bean注解用于在配置类中定义Bean。在配置类中，每个带有@Bean注解的方法将生成一个Bean，方法的返回值类型决定了Bean的类型，方法名默认为Bean的名称。

> 这种方式只会注入这个bean进去,而不会去扫描它内部的其他一些注入bean的注解

注意事项：确保配置类在组件扫描的路径下。

优点：易于管理，可在一个配置类中集中定义多个Bean，提高代码的可维护性。

缺点：与Spring框架产生了耦合。

### 3. 使用Java配置类和@BeanFactoryPostProcessor：

使用方法：在Java配置类中实现BeanFactoryPostProcessor接口，然后在`postProcessBeanFactory`方法中手动注册Bean。这种方式适用于更高级的用例，例如动态注册Bean。

注意事项：要确保实现了BeanFactoryPostProcessor接口的类被Spring扫描到。

优点：灵活，适用于高级用例和动态注册Bean。

缺点：相对复杂，需要更多的代码。

### 4. 使用XML配置文件：

使用方法：在XML文件中使用`<bean>`标签定义Bean，然后在启动类或配置类上使用@ImportResource注解导入XML配置文件。

注意事项：确保XML配置文件位于类路径下，且@ImportResource注解正确指向文件。

优点：与Spring框架的耦合相对较低，易于在不同项目中复用。

缺点：与Java配置相比，XML配置可读性较差，且需要额外维护一个配置文件。

总结：根据具体需求和场景选择合适的方式来定义和注册Bean。在大多数情况下，使用注解（如@Component、@Service等）和@Configuration类是最简单且推荐的方式，因为它们易于理解和维护。当有高级需求或需要动态注册Bean时，可以使用BeanFactoryPostProcessor。如果希望降低与Spring框架的耦合，可以考虑使用XML配置文件。



## 作用域



## 注入方式

在Spring Boot中，有几种常见的注入Bean的方式。每种方式都有其适用场景、优缺点以及注意事项。以下是主要的注入方式：

### @Autowired

可以使用@Autowired注解在**字段、构造函数或方法上进行依赖注入**。Spring会自动寻找与目标类型匹配的Bean并注入。

优点：

- 易于使用，代码简洁。
- 能在字段、构造函数和方法上使用。

缺点：

- 依赖于Spring特定的注解，降低了代码的可移植性。

注意事项：

- 如果没有找到与目标类型匹配的Bean，**Spring将抛出一个异常。为了避免这种情况，可以将@Autowired注解的required属性设置为false。**
- 当存在多个匹配的Bean时，**可以使用@Qualifier注解指定Bean的名称来消除歧义。**又或者说如果Bean有@Primary注解也可以优先被使用

### @Resource

@Resource注解是JavaEE提供的注解，可用于字段和方法上。它根据名称或类型查找匹配的Bean。

优点：

- 不依赖于Spring特定的注解，更具可移植性。
- 默认按名称查找Bean，当名称匹配失败时，再按类型查找。

缺点：

- **不能用于构造函数上。**
- 功能相对较少。

注意事项：

- 当存在多个匹配的Bean时，可以设置@Resource注解的name属性来消除歧义。

### @Inject

@Inject注解来自于Java的依赖注入规范（JSR-330），可用于字段、构造函数和方法上。它根据类型查找匹配的Bean。

优点：

- 不依赖于Spring特定的注解，具有更好的可移植性。
- 能在字段、构造函数和方法上使用。

缺点：

- **需要额外引入javax.inject依赖。**

注意事项：

- 如果没有找到与目标类型匹配的Bean，Spring将抛出一个异常。
- 当存在多个匹配的Bean时，可以使用@Named注解指定Bean的名称来消除歧义。

### 使用构造函数注入

通过在类的构造函数上添加@Autowired或@Inject注解，可以实现依赖注入。这是推荐的注入方式，因为它可以确保对象在创建时就已经注入了依赖，使得对象处于有效状态。

优点：

- 可以确保对象在创建时就已经注入了依赖，使得对象处于有效状态。
- 有助于实现不可变对象，提高代码的健壮性。

缺点：

- 当注入大量依赖时，构造函数可能变得复杂。

注意事项：

- **当使用构造函数注入时，如果只有一个构造函数，可以省略@Autowired或@Inject注解。**







## @Import注解

在Spring框架中，`@Import`注解用于导入其他的配置类。这个注解提供了一种方式来导入另一个或多个`@Configuration`类。以下是一些使用`@Import`注解的例子：

1. **导入配置类**：如果你有一些定义在其他配置类中的bean，你可以使用`@Import`注解来导入这些配置类。

```java
@Configuration
public class DatabaseConfig {
    @Bean
    public DataSource dataSource() {
        // 创建并返回数据源
    }
}

@Configuration
@Import(DatabaseConfig.class)
public class AppConfig {
    // 这个类现在可以使用DatabaseConfig类中定义的bean
}
```

2. **导入ImportSelector接口的实现**：`ImportSelector`是一个接口，它返回要导入的配置类的全类名。这个特性主要用于基于条件的配置。

```java
public class MyImportSelector implements ImportSelector {
    @Override
    public String[] selectImports(AnnotationMetadata importingClassMetadata) {
        // 返回要导入的类的全类名
        return new String[] {"com.example.DatabaseConfig"};
    }
}

@Configuration
@Import(MyImportSelector.class)
public class AppConfig {
    // 依据MyImportSelector的selectImports方法返回的类被导入
}
```

3. **导入ImportBeanDefinitionRegistrar接口的实现**：如果你想编程地注册bean，你可以实现`ImportBeanDefinitionRegistrar`接口，并使用`@Import`注解来导入它。

```java
public class MyBeanDefinitionRegistrar implements ImportBeanDefinitionRegistrar {
    @Override
    public void registerBeanDefinitions(AnnotationMetadata importingClassMetadata, BeanDefinitionRegistry registry) {
        // 在这里编程地注册bean
    }
}

@Configuration
@Import(MyBeanDefinitionRegistrar.class)
public class AppConfig {
    // MyBeanDefinitionRegistrar将会被调用，以便在运行时注册bean
}
```

总的来说，`@Import`注解在Spring中提供了一个强大的机制，可以用来导入配置类、普通类，或者基于`ImportSelector`和`ImportBeanDefinitionRegistrar`的更复杂的配置。

> 如果 @Import导入的是一个普通类的话,就仅仅是加载它的bean定义信息,还有他本身,如果是其他两种情况的话, 会加载它指定的配置类信息或者bean信息,但是本身都不会被注册为bean



## @Conditional注解

`@Conditional` 是 Spring Framework 4.0 引入的一个核心注解，用于基于满足某个特定条件来决定一个配置类、配置方法或者 Bean 是否需要被注册到 Spring 容器。

`@Conditional` 注解的主要作用是条件化地注册 Bean。在实际开发中，我们可能会遇到这样的需求：只有在满足特定条件（比如某个类在类路径上、某个系统属性存在等）的情况下，才需要注册某个 Bean。`@Conditional` 就是解决这种问题的。

使用 `@Conditional` 注解需要提供一个实现了 `Condition` 接口的类，这个类定义了条件逻辑。例如：

```java
@Conditional(MyCondition.class)
@Configuration
public class MyConfiguration {

    @Bean
    public MyBean myBean() {
        return new MyBean();
    }
}
```

在这个例子中，只有当 `MyCondition` 的 `matches` 方法返回 `true` 时，`MyConfiguration` 配置类才会被加载，`myBean` Bean 才会被创建。

下面是 `Condition` 接口的一个简单实现：

```java
public class MyCondition implements Condition {

    @Override
    public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
        // 这里可以定义复杂的条件逻辑
        return true; // 如果返回 true，那么带有 @Conditional 注解的配置或 Bean 就会被加载
    }
}
```

Spring Boot 还提供了一系列的 `Condition` 实现，比如 `@ConditionalOnClass`、`@ConditionalOnProperty` 等，这些都可以用于实现复杂的条件逻辑。

## AOP

AOP（Aspect-Oriented Programming，面向切面编程）是一种编程范式，用于将通用功能（如日志记录、安全检查等）从业务逻辑代码中分离出来，以提高代码的模块化程度。在 Spring Boot 中，可以使用 Spring AOP 框架实现 AOP 功能。以下是一些 AOP 相关的概念：

1. Aspect（切面）：封装横切关注点（如日志记录、事务管理等）的模块。切面可以包含多个通知（Advice）。

2. Advice（通知）：在特定连接点（Join Point）执行的动作。根据执行时机的不同，通知可以分为前置通知、后置通知、环绕通知、异常通知和最终通知。

3. Pointcut（切点）：定义在哪些连接点应用通知的表达式。切点确定了通知应该在何时、何地执行。

4. Join Point（连接点）：程序执行过程中的某个特定点，如方法调用、异常抛出等。连接点是通知实际应用的地方。

5. Target（目标对象）：被通知的对象，即包含业务逻辑的对象。

6. Proxy（代理）：由 AOP 框架创建的目标对象的代理，用于在调用目标方法前后插入通知的逻辑。

在 Spring Boot 中使用 AOP，通常需要进行以下步骤：

1. 引入依赖：首先，在 `pom.xml` 文件中引入 Spring AOP 相关依赖。

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aop</artifactId>
</dependency>
```

2. 定义切面：创建一个类，并使用 `@Aspect` 注解标注该类为切面。在切面类中，定义通知方法，并使用相应的通知注解（如 `@Before`、`@After`、`@Around` 等）标注这些方法。

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;

@Aspect
@Component
public class LoggingAspect {

    @Before("execution(* com.example.demo.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        System.out.println("Method called: " + joinPoint.getSignature().getName());
    }
}
```

在这个示例中，我们定义了一个名为 `LoggingAspect` 的切面，它包含一个前置通知方法 `logBefore`，用于在 `com.example.demo.service` 包下的所有方法执行前记录日志。

3. 配置 AOP：在 Spring Boot 中，AOP 通常是自动配置的。但是，在某些情况下，你可能需要自定义 AOP 的配置。在这种情况下，可以创建一个配置类，并使用 `@EnableAspectJAutoProxy` 注解开启 AOP 自动代理。

```java
import org.springframework.context.annotation.EnableAspectJAutoProxy;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableAspectJAutoProxy
public class AopConfig {
// 可以在此处自定义 AOP 相关的 Bean 或配置
}
```



### 通知

在通知方法中，可以使用一些特定的参数来获取关于目标方法和执行上下文的信息。以下是一些常用的通知方法参数：

1. JoinPoint：表示连接点的对象，提供了许多与目标方法相关的信息。一般在前置通知（`@Before`）、后置通知（`@After`）、异常通知（`@AfterThrowing`）和最终通知（`@AfterReturning`）中使用。`JoinPoint` 接口提供了以下一些常用方法：

    - `Signature getSignature()`：获取目标方法的签名信息。
    - `Object[] getArgs()`：获取目标方法的参数列表。
    - `Object getTarget()`：获取目标对象，即包含业务逻辑的对象。
    - `Object getThis()`：获取代理对象，即 AOP 框架创建的代理。
    - `SourceLocation getSourceLocation()`：获取源代码位置信息。

2. ProceedingJoinPoint：扩展自 `JoinPoint` 接口，表示可继续执行的连接点。一般在环绕通知（`@Around`）中使用。`ProceedingJoinPoint` 提供了一个额外的方法：

    - `Object proceed() throws Throwable`：执行目标方法。在环绕通知中，可以通过调用此方法来控制何时执行目标方法。

3. MethodInvocation：表示方法调用连接点的对象。它扩展自 `JoinPoint` 接口，并提供了一些额外的方法，如 `Method getMethod()`（获取目标方法的 `java.lang.reflect.Method` 对象）。在 Spring AOP 中，`MethodInvocation` 接口的实例通常作为 `JoinPoint` 或 `ProceedingJoinPoint` 的实现。

除了这些参数，还可以在通知方法中使用 `@annotation`、`@args`、`@target` 和 `@within` 等注解来绑定特定的目标方法参数、注解、目标对象类型等信息。例如，可以使用 `@annotation` 注解来获取目标方法上的自定义注解：

```java
@Before("execution(* com.example.demo.service.*.*(..)) && @annotation(myAnnotation)")
public void logBefore(JoinPoint joinPoint, MyAnnotation myAnnotation) {
    // ...
}
```

在这个示例中，`logBefore` 方法有两个参数：`JoinPoint` 和 `MyAnnotation`。`MyAnnotation` 参数使用 `@annotation` 注解绑定目标方法上的 `MyAnnotation` 注解。这样，在通知方法中，可以访问目标方法上的 `MyAnnotation` 注解及其属性值。

了解这些参数及其用法可以帮助你在通知方法中获取关于目标方法和执行上下文的详细信息，从而实现更复杂的横切关注点逻辑。

## 后置处理器

### 定义

Spring中有一些后置处理器，它们可以在Bean的生命周期中的不同阶段进行拦截，从而扩展或自定义Bean的行为。按照B**ean在Spring容器中被加载的顺序**，下面是一些常见的后置处理器及其用途和作用时机：

1. BeanDefinitionRegistryPostProcessor：
    用途：它允许在**Bean定义被加载到容器之前，修改或添加Bean定义**。可以用于动态注册Bean或修改Bean的元数据。
    作用时机：在所有Bean定义被加载到容器之前，调用postProcessBeanDefinitionRegistry()方法。举个例子

  ```java
  @Configuration
  public class AppConfig implements BeanDefinitionRegistryPostProcessor {
  
      @Override
      public void postProcessBeanDefinitionRegistry(BeanDefinitionRegistry registry) throws BeansException {
          // 创建一个新的 GenericBeanDefinition 实例
          GenericBeanDefinition beanDefinition = new GenericBeanDefinition();
  
          // 设置 bean 定义的属性
          beanDefinition.setBeanClassName("com.example.MyService");
          beanDefinition.setScope(BeanDefinition.SCOPE_SINGLETON);
  
          // 将 bean 定义注册到 BeanDefinitionRegistry
          String beanName = "myService";
          registry.registerBeanDefinition(beanName, beanDefinition);
      }
  
      @Override
      public void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException {
          // 不需要在这里做任何操作
      }
  }
  
  ```

  

2. BeanFactoryPostProcessor：
    用途：**它允许在Bean定义被加载且尚未实例化Bean之前修改Bean的定义**。主要用于修改Bean的配置元数据。
    作用时机：在所有Bean定义都已加载到容器且还未实例化Bean时，调用postProcessBeanFactory()方法。

  ```java
  @Component
  public class MyBeanFactoryPostProcessor implements BeanFactoryPostProcessor {
      @Override
      public void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException {
          System.out.println("我的beanFactoryPostProcessor被执行");
      }
  }
  ```

  

3. InstantiationAwareBeanPostProcessor：
    用途：**它允许在Bean实例化之前和之后进行自定义处理**，例如替换Bean的实例、改变属性值等。
    作用时机：在Bean实例化之前调用postProcessBeforeInstantiation()方法，实例化之后调用postProcessAfterInstantiation()方法，然后在设置属性前调用postProcessProperties()方法。

4. BeanPostProcessor：
    用途：它允许在Bean初始化的时候执行一些自定义逻辑，例如修改Bean的属性或执行其他配置。对所有的Bean都生效。
    作用时机：**在Bean的初始化方法（如afterPropertiesSet()或自定义的init-method）之前和之后**，分别调用postProcessBeforeInitialization()和postProcessAfterInitialization()方法。

5. DestructionAwareBeanPostProcessor：
    用途：**它允许在Bean销毁之前执行一些自定义逻辑，例如释放资源、清理缓存等**。
    作用时机：在Bean销毁之前调用postProcessBeforeDestruction()方法。

按照Bean的加载顺序，这些后置处理器都在Bean的生命周期中的不同阶段起作用。通过实现相应的接口并注册到Spring容器，可以灵活地扩展Bean的行为。

### spring默认提供的后置处理器

Spring框架默认提供了一些内置的后置处理器，这些后置处理器负责处理各种功能和任务。以下是一些常见的内置后置处理器及其用途：

1. ApplicationContextAwareProcessor：
用途：负责处理实现了ApplicationContextAware、ResourceLoaderAware、ApplicationEventPublisherAware和MessageSourceAware接口的Bean，为它们注入相应的依赖。

2. InitDestroyAnnotationBeanPostProcessor：
用途：**处理带有@PostConstruct和@PreDestroy注解的Bean，分别在Bean初始化后和销毁前执行相应的方法。**

3. AutowiredAnnotationBeanPostProcessor：
用途：**处理带有@Autowired、@Value和@Inject注解的Bean，负责自动装配Bean的属性、方法和构造函数。**

4. RequiredAnnotationBeanPostProcessor：
用途：处理带有@Required注解的Bean，确保标注了@Required注解的属性已经被设置，否则抛出异常。

5. CommonAnnotationBeanPostProcessor：
用途：**处理带有@Resource、@PostConstruct和@PreDestroy注解的Bean，分别负责依赖注入和在Bean初始化后、销毁前执行相应的方法。**

6. EventListenerMethodProcessor：
用途：处理带有@EventListener注解的方法，将它们注册为事件监听器。

7. DefaultEventListenerFactory：
用途：为@EventListener注解的方法提供默认的事件监听器实例。

8. ConfigurationClassPostProcessor (**BeanDefinitionRegistryPostProcessor**)：
用途：**处理带有@Configuration、@Bean、@ComponentScan、@Import和@PropertySource注解的配置类，负责解析和注册Bean定义。**

9. ScheduledAnnotationBeanPostProcessor：
用途：处理带有@Scheduled注解的方法，将它们注册为计划任务。

这些内置后置处理器由Spring框架自动注册，并在不同的生命周期阶段处理各种功能和任务。它们使得开发人员能够更加便捷地使用Spring框架的功能。

## 配置类与简化配置类

在阅读源码的过程中看到了这么两条语句

```
beanDef.setAttribute(CONFIGURATION_CLASS_ATTRIBUTE, "full");
beanDef.setAttribute(CONFIGURATION_CLASS_ATTRIBUTE, "lite");
```

经过查询后得到 一个是完整配置类,一个是简化配置类,  完整配置类是使用了@Configuration注解的类  而简化配置类是使用了 哪些组件注解的 比如 :

- `@Component`
- `@Service`
- `@Repository`
- `@Controller`
- 还有@import导入的类

完整配置类和简化配置类都可以在 Spring 中用于配置和创建 bean，但它们之间有一些关键区别：

1. 注解：完整配置类使用 `@Configuration` 注解，而简化配置类没有使用 `@Configuration` 注解。简化配置类通常使用 `@Component`、`@Service`、`@Repository` 或 `@Controller` 注解。

2. Bean 方法调用：在完整配置类中，`@Bean` 方法之间的调用会遵循 Spring 容器的单例规则，即调用 `@Bean` 方法时，容器会返回已经创建的 bean 实例（如果存在的话）。在简化配置类中，`@Bean` 方法之间的调用不会遵循单例规则，而是直接创建新的实例。这意味着在简化配置类中，如果一个 `@Bean` 方法调用另一个 `@Bean` 方法，它将会创建一个新的实例，而不是返回容器中已经存在的 bean 实例。

3. CGLIB 代理：**完整配置类会被 CGLIB 代理，以确保 `@Bean` 方法之间的调用遵循 Spring 容器的单例规则**。简化配置类不会被 CGLIB 代理，因此它们的 `@Bean` 方法之间的调用行为与普通的 Java 方法调用相同。

4. 适用场景：完整配置类主要用于集中管理和配置应用程序的 bean，通常会包含多个 `@Bean` 方法。简化配置类适用于将 bean 的定义散布在整个应用程序中，使其更接近使用 bean 的地方。这有助于保持代码的模块化和易于理解。

总之，完整配置类和简化配置类的主要区别在于它们处理 `@Bean` 方法之间调用以及代理方式的不同。完整配置类提供了更严格的管理和控制，而简化配置类提供了更轻量级和灵活的方式来配置和定义 bean。在实际应用中，可以根据需求和场景选择使用哪种配置类。

完整配置类可以转换成简单配置类

```java
@Configuration(
    proxyBeanMethods = false   //这样就不会生成代理类,也不会维护里面方法的相互依赖关系,每次调用方法都是生成一个新的对象
)
```



# spring boot 



## 多余文件介绍

从官网下过来的项目中会多处一部分跟maven相关的东西,我们来看看吧

Spring Boot项目中的`.mvn`文件夹以及`mvnw`和`mvnw.cmd`文件是Maven Wrapper的一部分。Maven Wrapper是一个方便的工具，让开发者可以在没有预先安装Maven的情况下运行Maven项目。

以下是这些文件的具体用途：

1. `.mvn`：这是一个文件夹，通常包含`wrapper`子文件夹以及一个`maven-wrapper.properties`文件，这个文件包含了Maven分发包的URL，Maven Wrapper会从这个URL下载对应版本的Maven。

2. `mvnw`：这是一个Unix shell脚本，用于在Linux或Mac操作系统上运行Maven命令。使用这个脚本，你可以不必在你的机器上预先安装Maven，而是直接运行Maven项目。

3. `mvnw.cmd`：这是一个Windows批处理文件，用于在Windows操作系统上运行Maven命令。与`mvnw`脚本类似，使用这个批处理文件，你可以不必在你的机器上预先安装Maven，而是直接运行Maven项目。

这些文件的主要优点是它们使项目能够自我包含，并且不需要开发者预先安装特定版本的Maven。而且，由于这些文件将Maven的版本和分发包的URL存储在源代码中，因此它们还确保了项目的构建过程的一致性，无论是在不同的开发环境还是在持续集成服务器上。



## 自动配置原理

Spring Boot 的自动配置是它的一个核心功能，它通过预先定义的默认配置和约定优于配置（Convention over Configuration）的原则，简化了应用程序的配置。自动配置的原理主要依赖以下几个关键技术：

1. 条件注解：Spring Boot 使用条件注解（如 `@ConditionalOnClass`、`@ConditionalOnBean`、`@ConditionalOnMissingBean` 等）来根据当前应用程序上下文和类路径的情况来决定是否应用某个配置。这些注解使得 Spring Boot 能够在满足特定条件时自动配置所需的组件。

2. 自动配置类：Spring Boot 提供了许多自动配置类，它们是带有 `@Configuration` 注解的 Java 配置类，包含了一系列预定义的默认配置。这些自动配置类通常以 `AutoConfiguration` 结尾，例如 `DataSourceAutoConfiguration`、`WebMvcAutoConfiguration` 等。这些自动配置类会在应用程序启动时被加载，并根据条件注解决定是否应用这些默认配置。

3. `spring.factories` 文件：`spring.factories` 文件是 Spring Boot 的一个关键配置文件，它位于 `META-INF` 目录下。该文件定义了许多自动配置类和启用器，它们在应用程序启动时被 Spring Boot 自动发现和加载。自动配置类和启用器都是通过 `org.springframework.boot.autoconfigure.EnableAutoConfiguration` 键列出的。

4. `@EnableAutoConfiguration` 注解：这个注解通常在 Spring Boot 的主配置类或启动类上使用（通过 `@SpringBootApplication` 注解间接启用，因为 `@SpringBootApplication` 包含了 `@EnableAutoConfiguration`）。该注解负责激活自动配置功能，并从 `spring.factories` 文件中加载自动配置类。

整个自动配置过程如下：

1. 当您的应用程序启动时，Spring Boot 会加载带有 `@SpringBootApplication` 注解的主类。
2. `@SpringBootApplication` 注解包含了 `@EnableAutoConfiguration` 注解，这个注解会激活自动配置功能。
3. Spring Boot 读取 `spring.factories` 文件，**加载并实例化其中定义的自动配置类**。
4. 对于每个自动配置类，Spring Boot 根据条件注解的结果决定是否应用它们。
5. 在满足条件的情况下，自动配置类会将默认配置和相关组件注册到应用程序上下文中。

通过这个自动配置原理，Spring Boot 能够在适当的时机为应用程序提供合适的默认配置，从而简化开发过程。当然，也可以覆盖这些默认配置，以满足特定的需求。



## 配置文件

Spring Boot中的配置文件是用于配置应用程序的属性和参数的文件。Spring Boot支持多种类型的配置文件，包括属性文件、**YAML文件**、JSON文件等. 配置文件可以包含应用程序的所有配置参数，例如数据库连接信息、日志配置、服务器端口等。这些参数可以通过@ConfigurationProperties注解和@Value注解在应用程序中访问。

Spring Boot 提供了许多有用的特性，以简化配置文件的使用。以下是一些配置文件中的特殊用法：

### 配置文件的多环境支持：

Spring Boot **支持使用不同的配置文件来区分不同的环境**（如开发、测试和生产环境）。您可以在 `application.yml` 或 `application.properties` 文件中使用 `spring.profiles.active` 属性来激活特定的环境配置文件。例如，在 `application.yml` 文件中：

```yaml
spring:
  profiles:
    active: dev
```

这将激活名为 `application-dev.yml` 的配置文件。您还可以通过命令行参数或环境变量来覆盖此属性。

### 配置文件中的占位符

您可以在配置文件中使用 `${...}` 占位符引用其他属性。例如：

```properties
app.message=Hello, Spring Boot!
app.greeting=${app.message} Welcome to our application!
```

在这个例子中，`app.greeting` 的值将包含 `app.message` 的值。

### 配置文件的优先级

Spring Boot 允许您将配置文件放在不同的位置，如项目的根目录、`config/` 目录、类路径等。不同位置的配置文件具有不同的优先级。例如，项目根目录下的 `application.properties` 文件的优先级高于类路径下的 `application.properties` 文件。这意味着在多个位置定义相同的属性时，具有较高优先级的配置文件中的值将覆盖较低优先级的配置文件中的值。

### 使用 YAML 配置文件中的锚点和别名

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

### 获取pom.xml的环境变量

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



> 需要注意的是,配置文件里面的变量不区分大小写,环境变量也是

## 配置文件读取

在 Spring Boot 中，常用的配置文件格式有两种：`.properties` 和 `.yml`（或 `.yaml`）。Spring Boot 自动加载项目根目录下的 `application.properties` 或 `application.yml` 文件作为默认的配置文件。您可以使用以下方式来读取配置文件中的值：

### 使用 `@Value` 注解

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

### 使用 `@ConfigurationProperties` 注解

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

### 使用 `Environment` 对象

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

## 配置文件优先级

Spring Boot 允许将配置文件放在多个位置，它们具有不同的优先级。配置文件可以是 `application.properties` 或 `application.yml` 格式。以下是 Spring Boot 在寻找配置文件时的默认搜索顺序：

1. 当前目录下的 `/config` 子目录。
2. 当前目录。
3. 类路径下的 `/config` 包。
4. 类路径的根目录。

在这个顺序中，位于靠前位置的配置文件会优先加载，并且可能会覆盖后续位置的相同配置。例如，如果当前目录下的 `application.properties` 文件中有一个 `server.port` 配置，而类路径下的 `application.properties` 文件中也有一个 `server.port` 配置，那么当前目录下的配置会生效。

在这些位置中，类路径下的配置文件通常是打包在 JAR 文件中的。在运行 JAR 文件时，Spring Boot 会自动加载 JAR 包内的配置文件。你可以将配置文件放在 `src/main/resources` 或 `src/main/resources/config` 目录下，Maven 或 Gradle 会在构建过程中将它们打包到 JAR 文件中。

总之，是的，Spring Boot 会在运行时加载 JAR 包中的配置文件。

## 配置源的优先级

在Spring Boot中，配置文件的优先级是有明确规定的。Spring Boot将从多个位置读取配置，并根据特定的优先级对它们进行排序，高优先级的配置将覆盖低优先级的配置。

以下是一些主要的配置源及其优先级，从高到低：

1. 命令行参数
2. `SPRING_APPLICATION_JSON`属性中的属性
3. `ServletConfig`初始化参数
4. `ServletContext`初始化参数
5. 来自`java:comp/env`的JNDI属性
6. Java系统属性（`System.getProperties()`）
7. 操作系统环境变量
8. 只包含随机属性的`random.*`属性文件
9. 位于当前目录的`.env`文件
10. 如果不是`jar`包运行，位于应用程序目录的`application-{profile}.properties`或`application-{profile}.yml`以及`application.properties`或`application.yml`
11. 如果是`jar`包运行，位于应用程序`jar`包内部的`application-{profile}.properties`或`application-{profile}.yml`以及`application.properties`或`application.yml`
12. 在`@Configuration`类中通过`@PropertySource`注解指定的属性源
13. 默认属性（使用`SpringApplication.setDefaultProperties`指定）

以上是一些主要的配置源，实际上Spring Boot还支持更多的配置源，包括云服务的配置等。

## 自定义starter

### 创建一个空maven项目

修改配置文件如下:  分别配置坐标 和 引入依赖

```xml
 <groupId>com.djm</groupId>
    <artifactId>socket-spring-boot-starter</artifactId>
    <version>1.0-SNAPSHOT</version>
    
        <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-autoconfigure</artifactId>
            <version>2.7.11</version>
        </dependency>
    </dependencies>

```

### 创建自动配置类

```java
@Configuration
@Import(MyServerSocket.class)  // 导入要配置的东西
public class SocketAutoConfiguration {

}

// 要往容器中自动放入的bean
public class MyServerSocket {
    
    // 后续做准备
    String hello;
    
    public void sayHello(){
        System.out.println(hello);
        System.out.println("hello world");
    }
    
    public void setHello(String hello){
        this.hello = hello;
    }
}


```

### 创建META-INF/spring.factories文件

springboot项目在启动的时候,有个注解导入了一个自动扫描所有jar包下面的 META-INF/spring.factories文件

```
org.springframework.boot.autoconfigure.EnableAutoConfiguration=com.djm.SocketAutoConfiguration
```

这里是一对键值组合, 键通常是一个接口或者一个注解，值则是一组实现了该接口或被该注解标记的类，用逗号分隔。不同的键值对做不同的事情, 以下是一些常见的键：

1. `org.springframework.boot.autoconfigure.EnableAutoConfiguration`：这是最常见的键，它用于指定应该由 Spring Boot 自动配置的类。当 Spring Boot 应用启动时，这些类将会被实例化，并且它们中定义的任何 bean 都会被添加到 Spring 应用上下文中。
2. `org.springframework.context.ApplicationContextInitializer`：这个键用于指定应该在 Spring 应用上下文初始化期间执行的类。这些类可以用来进行一些自定义的初始化操作。
3. `org.springframework.context.ApplicationListener`：这个键用于指定应该在 Spring 应用上下文中注册的 ApplicationListener 类，这些类可以用来监听和处理 Spring 发布的各种事件。
4. `org.springframework.boot.SpringApplicationRunListener`：这个键用于指定在 Spring Boot 应用启动期间应该调用的监听器类。这些监听器可以用来自定义 Spring Boot 的启动过程。

### 打包,安装,发布(如果有需要的话)

```
mvn package
mvn install
mvn deploy
```

### 使用这个starter

新建一个springboot项目导入依赖

```
<dependency>
			<groupId>com.djm</groupId>
			<artifactId>socket-spring-boot-starter</artifactId>
			<version>1.0-SNAPSHOT</version>
		</dependency>
```

我们可以查看是否自动注册了这个bean

```
@SpringBootApplication
public class SocketAutoConfiguration1 {

    public static void main(String[] args) {
        ConfigurableApplicationContext run = SpringApplication.run(SocketAutoConfiguration.class);
        MyServerSocket bean = run.getBean(MyServerSocket.class);
        bean.sayHello();  // 输出  null 和 hello world  代表配置成功
    }

}
```

**需要注意的是,如果我们项目里面有了application.properties文件的话,jar包里面的application.properties是不会生效的,  比如我们在starter里面想要使用starter里面定义的配置文件的话这样是不行的, 而且也不推荐啊,我们可以使用一个资源类,然后给默认值不就行了?**,比如:

修改代码

```java
@ConfigurationProperties(prefix = "my")   //定义好资源类
public class MyProperties {
    public String hello = "我是jar包里面的hello"; // 定义好默认值, 如果用户配置文件里面有 my.hello 自然可以覆盖  

    public String getHello() {
        return hello;
    }

    public void setHello(String hello) {
        this.hello = hello;
    }
}

@Configuration
@EnableConfigurationProperties(MyProperties.class)
public class SocketAutoConfiguration {

    @Bean
    public MyServerSocket myServerSocket(MyProperties properties) {
        MyServerSocket myServerSocket = new MyServerSocket();
        myServerSocket.setHello(properties.hello);
        return myServerSocket;
    }
}





```



## 监听器

### 常用监听器与事件

Spring Boot中的监听器和事件是基于Spring框架的事件驱动模型。下面列出了一些常见的监听器和事件：

监听器（Listener）：

1. ApplicationListener：这是一个通用的监听器接口，用于监听各种类型的事件。你可以实现此接口并根据需要定义自己的监听器。

2. ServletContextListener：这是Java Servlet规范中的监听器，用于在Web应用程序的生命周期中监听ServletContext的创建和销毁事件。

3. HttpSessionListener：这是Java Servlet规范中的监听器，用于在Web应用程序的生命周期中监听HttpSession的创建和销毁事件。

4. ServletRequestListener：这是Java Servlet规范中的监听器，用于在Web应用程序的生命周期中监听ServletRequest的创建和销毁事件。

事件（Event）：

1. ContextRefreshedEvent：当ApplicationContext初始化或刷新时触发此事件。

2. ContextStartedEvent：当ApplicationContext启动时触发此事件。

3. ContextStoppedEvent：当ApplicationContext停止时触发此事件。

4. ContextClosedEvent：当ApplicationContext关闭时触发此事件。

5. ServletContextInitializedEvent：当ServletContext初始化时触发此事件。

6. ServletContextDestroyedEvent：当ServletContext销毁时触发此事件。

7. HttpSessionCreatedEvent：当HttpSession创建时触发此事件。

8. HttpSessionDestroyedEvent：当HttpSession销毁时触发此事件。

9. ServletRequestInitializedEvent：当ServletRequest创建时触发此事件。

10. ServletRequestDestroyedEvent：当ServletRequest销毁时触发此事件。

11. ApplicationEnvironmentPreparedEvent：在应用环境准备完成且ApplicationContext创建之前触发此事件。

12. ApplicationPreparedEvent：在ApplicationContext创建完成但尚未刷新时触发此事件。

13. ApplicationReadyEvent：在ApplicationContext刷新并启动后触发此事件，此时应用已经准备好接受请求。

14. ApplicationFailedEvent：当应用启动失败时触发此事件。

15. SpringApplicationEvent：**这是所有Spring Boot事件的基类，可以用于监听所有Spring Boot相关事件**。

通过实现监听器并监听相应的事件，你可以在应用程序的生命周期中的特定时刻执行特定操作。此外，你还可以创建自定义事件和监听器，以满足特定的业务需求。

### springboot启动过程中发出的事件

Spring Boot在启动过程中会主动触发一系列事件，这些事件通常用于在应用程序生命周期的不同阶段执行特定的操作。以下是Spring Boot启动过程中的一些关键事件：

1. ApplicationStartingEvent：在Spring Boot应用程序开始运行，但任何处理开始之前触发。这是启动过程中触发的第一个事件。

2. ApplicationEnvironmentPreparedEvent：在应用环境准备完成且ApplicationContext创建之前触发。此时，应用已经加载了配置文件并准备好了环境。

3. ApplicationContextInitializedEvent：在ApplicationContext准备好后触发，但在它被刷新前。此时，已经注册了bean定义，但bean实例还没有被创建。

4. ApplicationPreparedEvent：在ApplicationContext创建完成但尚未刷新时触发。此时，所有bean定义已经加载到容器中，但bean实例尚未创建。

5. ContextRefreshedEvent：当ApplicationContext初始化或刷新时触发。此时，所有bean已经被创建并初始化。 **从这一步开始,我们通过注解定义的事件监听器才会响应事件**

6. ServletWebServerInitializedEvent：在嵌入式Servlet容器（如Tomcat、Jetty等）初始化完成时触发。此时，应用程序已经准备好处理HTTP请求。

7. ApplicationStartedEvent：在ApplicationContext刷新并启动后触发，但在任何应用程序和命令行运行器（ApplicationRunner和CommandLineRunner）开始之前。此时，应用程序已经准备好处理业务逻辑。

8. ApplicationReadyEvent：在所有应用程序和命令行运行器（ApplicationRunner和CommandLineRunner）执行完成后触发。此时，应用已经准备好接受请求，此事件表明应用已完全启动并处于运行状态。

9. ApplicationFailedEvent：当应用启动失败时触发。这个事件只有在启动过程中出现异常时才会触发。

通过监听这些事件，你可以在应用程序的生命周期中的特定时刻执行特定操作。例如，在`ApplicationReadyEvent`触发时执行一些初始化任务，或者在`ApplicationFailedEvent`触发时执行错误处理操作。

### 创建监听器

#### 基于@EventListener 

Spring Boot中的事件监听器允许您对应用程序中发生的事件进行响应。这些事件包括应用程序生命周期事件、自定义事件等。要使用事件监听器，请遵循以下步骤：

1. 创建事件：
   如果您要监听的是自定义事件，首先需要创建一个事件类。自定义事件类需要继承`org.springframework.context.ApplicationEvent`。

例如：

```java
public class CustomEvent extends ApplicationEvent {
    private String message;

    public CustomEvent(Object source, String message) {
        super(source);
        this.message = message;
    }

    public String getMessage() {
        return message;
    }
}
```

2. 创建事件监听器：
   在需要监听事件的类中创建一个方法，该方法将在事件发生时被调用。然后使用`@EventListener`注解标记此方法，并指定要监听的事件类型。

例如：

```java
@Component
public class CustomEventListener {

    @EventListener
    public void handleCustomEvent(CustomEvent event) {
        System.out.println("Received custom event: " + event.getMessage());
    }
}
```

3. 发布事件：
   要触发事件，需要将事件发布到应用程序上下文中。您可以通过注入`org.springframework.context.ApplicationEventPublisher`并调用其`publishEvent()`方法来实现。

例如：

```java
@Service
public class CustomEventPublisher {
    private final ApplicationEventPublisher eventPublisher;

    public CustomEventPublisher(ApplicationEventPublisher eventPublisher) {
        this.eventPublisher = eventPublisher;
    }

    public void publishCustomEvent(String message) {
        CustomEvent event = new CustomEvent(this, message);
        eventPublisher.publishEvent(event);
    }
}
```

4. 使用事件监听器：
   现在您已经准备好使用事件监听器。当您需要触发事件时，只需调用`CustomEventPublisher`中的`publishCustomEvent()`方法，事件监听器将自动响应事件。

例如，在Controller类中使用`CustomEventPublisher`：

```java
@RestController
public class CustomEventController {

    private final CustomEventPublisher customEventPublisher;

    public CustomEventController(CustomEventPublisher customEventPublisher) {
        this.customEventPublisher = customEventPublisher;
    }

    @GetMapping("/triggerEvent")
    public String triggerEvent() {
        customEventPublisher.publishCustomEvent("Hello, this is a custom event!");
        return "Event triggered";
    }
}
```

通过上述步骤，您可以在Spring Boot应用程序中使用事件监听器来监听和响应特定事件。

#### 基于接口

有些事件并不支持上面那种方法,当然支持上面那种方法的,一定可以基于接口使用, 我们来定义一个session创建与销毁的监听器

```java

import org.springframework.stereotype.Component;

import javax.servlet.http.HttpSessionEvent;
import javax.servlet.http.HttpSessionListener;

@Component
public class MyHttpSessionEventListener implements HttpSessionListener {
    @Override
    public void sessionCreated(HttpSessionEvent se) {
        System.out.println("session创建: " + se.getSession().getId());
    }

    @Override
    public void sessionDestroyed(HttpSessionEvent se) {
        System.out.println("session销毁: " + se.getSession().getId());
    }
}
```





## actuator

用来检测项目运行状况

搭配spring-boot-admin **来可视化的监控** spring-boot 程序的运行状态







# springMVC



## 异常类



### HttpMessageNotReadableException

在 Spring Boot 应用程序中，HttpMessageNotReadableException 异常通常代表请求的消息无法读取或解析。这个异常通常是由于以下原因之一导致的：

1. 请求的 Content-Type 不正确：如果请求的 Content-Type 不正确，例如请求头中的 Content-Type 是 application/json，但请求体中的数据格式不是 JSON 格式，则会导致 HttpMessageNotReadableException 异常。
2. 请求体中的数据格式不正确：如果请求体中的数据格式不正确，例如请求体中的 JSON 数据格式不符合要求，或者请求体中缺少必要的属性等，也会导致 HttpMessageNotReadableException 异常。
3. 请求体中的数据长度不正确：如果请求体中的数据长度超出了服务器预期的范围，也可能导致 HttpMessageNotReadableException 异常。

当发生 HttpMessageNotReadableException 异常时，Spring Boot 会自动返回一个 HTTP 400 Bad Request 响应，提示客户端请求的消息无法读取或解析。

## 异常处理

通常使用controlleradvice来捕获异常

```java
@RestControllerAdvice
public class MyExceptionHandler {

    @ExceptionHandler(Exception.class)
    public String handler(Exception exception){ 
       return exception.getMessage();
    }

}
```

总结一下在`@ExceptionHandler`方法中可以使用的参数：

1. 异常参数：您可以将处理的异常类或其基类（如`Exception`、`RuntimeException`等）作为参数传递。这是必须的，用于捕获异常信息。

2. `HttpServletRequest`：您可以将`HttpServletRequest`对象作为参数，以便访问与请求相关的信息，例如获取请求参数、请求头等。

3. `HttpServletResponse`：您可以将`HttpServletResponse`对象作为参数，以便操作响应对象，例如设置响应状态码、响应头等。

4. `WebRequest`或`NativeWebRequest`：您可以使用这些对象以一种与底层技术无关的方式访问请求和响应的属性。

5. `Locale`：可以使用`Locale`对象获取客户端的区域设置信息。

6. `Model`：可以将`Model`对象作为参数，以便向视图添加属性。在返回`ModelAndView`对象时，这可能会派上用场。

7. `@ModelAttribute`：虽然在异常处理器中使用`@ModelAttribute`的情况较少，但您可以在需要时将带有`@ModelAttribute`注解的参数添加到方法中。

请注意，一些常见的参数，如`@RequestParam`、`@PathVariable`、`@RequestHeader`等，在异常处理器方法中是不支持的。需要使用`HttpServletRequest`对象来获取这些值。

**如果有多个异常处理器,最终只有一个异常处理器会生效**,根据优先级来.



## 过滤器

下面是定义过滤器的几种方式

### FilterRegistrationBean

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

### @Component` 和 `@Order 注解

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
        
        // 这里是是请求处理结束了的位置
    }

    @Override
    public void destroy() {
        // 清理操作，例如释放资源、清理缓存等
    }
}
```

> 上面的方式适用于传统的springMVC,下面这两种可以用于springboot

### 使用 `@WebFilter` 注解：

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



## 拦截器

### 定义

在 Spring MVC 中，`HandlerInterceptor` 接口定义了三个方法，用于在请求处理的不同阶段执行自定义操作。这些方法分别是：

1. `preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)`：在处理器（即 Controller 方法）执行之前调用。如果该方法返回 `true`，则请求继续向下执行；如果返回 `false`，则请求处理停止，不会调用后续的拦截器和处理器。这个方法通常用于权限控制、身份验证和请求参数校验等。

2. `postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView)`：在处理器执行之后、视图渲染之前调用。这个方法可以用来修改数据模型、处理异常等。注意，如果 `preHandle` 返回 `false`，则不会调用 `postHandle`。

3. `afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex)`：在请求处理完成后调用，即在视图渲染之后。这个方法通常用于清理资源、记录日志、监控性能等。**即使在请求处理过程中发生异常，这个方法也会被调用。注意，如果 `preHandle` 返回 `false`，则不会调用 `afterCompletion`。**

实现 `HandlerInterceptor` 接口时，你可以根据需要重写这些方法以实现自定义的请求拦截和处理逻辑。在实际应用中，你通常会继承 `HandlerInterceptorAdapter` 类，它提供了默认的空实现，这样你只需要重写需要的方法即可。

### 使用

创建拦截器

```java
public class MyInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        return true;
    }

    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        System.out.println("postHandle");
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        System.out.println("afterCompletion");
    }
}
```

注册

```java
@Configuration(proxyBeanMethods = false)
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new MyInterceptor()).addPathPatterns("/**");
    }
}
```

## 过滤器与拦截器的区别

过滤器（Filter）和拦截器（Interceptor）都是用于处理Web应用程序中的请求和响应的。它们之间的主要区别在于作用范围、处理时机和功能。

1. 作用范围：

   - 过滤器（Filter）是基于Java Servlet规范的，适用于所有Java Web应用程序。它可以拦截所有进入Servlet容器的HTTP请求和响应，对它们进行预处理和后处理。
   - 拦截器（Interceptor）是Spring MVC特有的，仅适用于使用Spring MVC框架的Web应用程序。它在Spring MVC处理请求的过程中起作用，主要拦截Controller方法的调用。

2. 处理时机：

   - 过滤器（Filter）在Servlet容器层面处理请求，所以它在请求进入Web应用程序之前和离开Web应用程序之后都起作用。因此，过滤器可以在请求被处理之前和响应被发送之前进行一些操作。
   - 拦截器（Interceptor）在Spring MVC处理请求的过程中起作用，它在请求到达Controller方法之前、Controller方法处理完成后、视图渲染完成之后都可以执行相应的操作。

3. 功能：

   - 过滤器（Filter）可以用于对请求和响应进行通用处理，例如字符编码转换、安全检查、压缩响应等。
   - 拦截器（Interceptor）更适用于处理与应用程序业务逻辑相关的操作，例如登录验证、权限控制、性能监控等。由于拦截器是Spring MVC特有的，所以它可以方便地访问Spring的依赖注入（DI）功能，以及其他Spring MVC组件。

总之，过滤器（Filter）和拦截器（Interceptor）都可以实现类似的功能，但由于它们在不同的处理阶段和层次起作用，所以它们的使用场景和优缺点也有所不同。根据具体的需求和应用程序架构，可以选择使用过滤器、拦截器或者它们的组合来实现所需的功能。

## 权限校验的几种方式

### 过滤器



### 拦截器



### AOP + RestControllerAdvice

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



## 请求响应流程

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

上面这个步骤其实还少了拦截器

## 自定义资源处理

springboot默认帮我们配置了不少的资源路径

```java
private static final String[] CLASSPATH_RESOURCE_LOCATIONS = new String[]{"classpath:/META-INF/resources/", "classpath:/resources/", "classpath:/static/", "classpath:/public/"};
private String staticPathPattern = "/**"; 
```

当然如果不想使用就直接禁用掉,这样就省去了一个资源处理器

```yaml
spring:
  web:
    resources:
      add-mappings: false
```

然后自定义

```java
@Configuration(proxyBeanMethods = false)
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/static/**").addResourceLocations("classpath:/static/"); // 这样的话,所有的/static请求都会去使用资源路径,也不一定,如果有controller的路径跟我们对上了,那肯定那个处理器优先,里面有一套排序规则的
    }
}

```

这里有个高级的用法就是addResourceLocations里面可以使用文件系统的路径,这就方便很多了啊,我们可以使用配置文件的方法很灵活的放置和取资源

```java
@Configuration(proxyBeanMethods = false)
public class WebConfig implements WebMvcConfigurer {
    
    @Value("${filePath}")
    String path;
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/static/**").addResourceLocations("file:"+path+"/"); 
    }
}
```



### 注意点

* 如果有多个资源处理器能够处理这个路径, 那么会选择最符合的资源处理器去处理这个请求, 但是如果两个资源处理器的优先级一样,那就是谁先定义谁被使用,  而且在springboot中,永远有一个/**的默认处理器为我们兜底,前提是你没关闭它

* **如果一个资源处理器被选择了, 即使它不能处理这个路径的资源,那么它就会抛出404,而不是交给下一个能处理这个资源的处理器**,比如你定义了两个/** 和 /static 路径的资源处理器,  当你处理/static路径的时候  会选择 /static路径的资源处理器, 如果它不能处理,也不会去选择/**处理器了,而是响应404回去

  



## 自定义404异常处理

404在springMVC中分为两种, 第一种是没有处理器对应, 第二种是资源处理器里面没有对应资源, 如果看过源码的话,就知道springboot默认给我们提供一个兜底的资源处理器,它能够处理任何路径, **因此就算开启找不到处理器抛出异常这个选项, ControllerAdvice也没有机会去捕获异常,因为无论如何都有资源处理器去处理,** 除非你放弃使用资源处理器,然后开启没有异常处理抛出异常

```yaml
spring:
  mvc:
    throw-exception-if-no-handler-found: true
  web:
    resources:
      add-mappings: false
```

这样的话,能够使用ControllerAdvice去处理404异常

但是我们一般要使用静态资源,所有我们**一般是重写一个ErrorController 去处理404异常**

```java
@RestController
public class MyErrorController implements ErrorController {

    @RequestMapping("/error")
    public String notFound(HttpServletRequest httpServletRequest){
        // 这里要注意,如果是springboot3.0的话 就是jakarta开头了
      if(httpServletRequest.getAttribute("javax.servlet.error.status_code").equals(HttpStatus.NOT_FOUND.value()))
        {
            return "404 not found";
        }

        return "500 error";
    }

}
```





## 自定义数据转换

### Converter和Formatter

Converter

```java
import org.springframework.core.convert.converter.Converter;

public class StringToPersonConverter implements Converter<String, Person> {

    @Override
    public Person convert(String source) {
        int id = Integer.parseInt(source);
        return new Person(id);
    }
}

```

formatter

```java
import org.springframework.format.Formatter;

import java.text.ParseException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class LocalDateFormatter implements Formatter<LocalDate> {

    private DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");

    @Override
    public LocalDate parse(String text, Locale locale) throws ParseException {
        return LocalDate.parse(text, formatter);
    }

    @Override
    public String print(LocalDate object, Locale locale) {
        return formatter.format(object);
    }
}

```

注册他们

```java
@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addFormatters(FormatterRegistry registry) {
        registry.addFormatter(new LocalDateFormatter());
        registry.addConverter(new StringToPersonConverter());
    }
}

```



### HttpMessageConverter

```java
public class MyHttpMessageConvert extends AbstractHttpMessageConverter<User> {

    public MyHttpMessageConvert(){
        super(MediaType.APPLICATION_JSON);
    }

    @Override
    protected boolean supports(Class<?> clazz) {
        return User.class == clazz;
    }

    @Override
    protected User readInternal(Class<? extends User> clazz, HttpInputMessage inputMessage) throws IOException, HttpMessageNotReadableException {
        System.out.println("我的httpMessage被执行");
        return new ObjectMapper().readValue(inputMessage.getBody(),clazz);
    }

    @Override
    protected void writeInternal(User user, HttpOutputMessage outputMessage) throws IOException, HttpMessageNotWritableException {
        System.out.println("我的httpMessage被执行");
        new ObjectMapper().writeValue(outputMessage.getBody(),user);
    }
}

```



注册

```java
@Configuration
public class WebConfig implements WebMvcConfigurer {

    /*@Override
    public void configureMessageConverters(List<HttpMessageConverter<?>> converters) {
        converters.add(new MyHttpMessageConvert());
    }*/
    @Override
    public void extendMessageConverters(List<HttpMessageConverter<?>> converters) {  // 注意这里要使用这个,如果使用上面这个,那么就只会留下我们自己的
        converters.add(0,new MyHttpMessageConvert());  // 这里我们把它放在最前面,增加优先级
    }
}
```



### 区别

`Converter`：
1. 它是Spring的一个核心接口，用于在类型之间进行转换，例如在**表单数据绑定到Java对象**时，或者在@PathVariable注解的参数转换时。
2. 它主要用于将一种数据类型转换为另一种数据类型。例如，将一个字符串转换为一个日期对象或自定义类型。
3. `Converter`通常在数据绑定或类型转换过程中使用。
4. **它不关心HTTP请求或响应的内容，仅关注类型之间的转换。**

`HttpMessageConverter`：
1. 它是Spring MVC中的一个接口，**用于处理HTTP请求和响应中的内容**。
2. 它主要用于将请求体中的数据转换为Java对象（反序列化），或者将Java对象转换为响应体中的数据（序列化）。
3. `HttpMessageConverter`通常与`@RequestBody`和`@ResponseBody`注解一起使用，**以将请求和响应中的数据与Java对象进行转换。**
4. 它关注HTTP请求和响应的内容，以及将数据与Java对象之间进行序列化和反序列化。

总结一下：
- `Converter`主要用于在类型之间进行转换，例如将字符串转换为自定义对象。它通常在数据绑定过程中使用，与HTTP请求和响应的内容无关。
- `HttpMessageConverter`主要用于处理HTTP请求和响应中的数据。它负责将请求体中的数据转换为Java对象，以及将Java对象转换为响应体中的数据。它与`@RequestBody`和`@ResponseBody`注解一起使用。

## 跨域问题

```
 @Configuration
public class WebConfig implements WebMvcConfigurer {
	@Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/file/**").allowedOrigins("*").allowedMethods("*");
    }
}
```



## 注意点

1. springMVC中有很多的一次性注解,它会将输入流里面东西读出来,因此在使用的时候要特别注意,不要多次使用,比如@RequestBody这种
2. 使用HttpMessageConverter 放入自己的转换器的时候,要注意extendMessageConverters() 和 configureMessageConverters() 的区别

# Mybatis-Plus

## 导入依赖

```
<dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
            <version>3.5.3.1</version>
        </dependency>
```

## 配置数据源

```
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mybatis?useUnicode=true&characterEncoding=utf-8&useSSL=false
    username: root
    password: root
    driver-class-name: com.mysql.cj.jdbc.Driver
```



## 命名规则

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

## 属性名字或者类名与关键字冲突

使用TableName 和 TableField

```java
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



## 代码生成

导入依赖,这两个搭配才能生效

```
 <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>2.3.0</version>
        </dependency>
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

**他就会帮我们生成好实体类与mapper还有service,还有controller**

> 推荐使用插件而不是这种方式





## 映射文件编写

映射文件是MyBatis框架中用于描述数据库操作和Java对象之间映射关系的XML文件。它包含了执行SQL操作所需的各种信息，如SQL语句、输入参数、返回结果等。映射文件可以将SQL语句和Java代码分离，使得代码更易于维护和阅读。映射文件通常以`.xml`为扩展名，并位于项目的资源文件夹（如`src/main/resources`）中。

映射文件的基本结构如下：

```xml
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.example.mapper.YourMapper">
    <!-- SQL操作映射，例如select、insert、update、delete等 -->
</mapper>
```

1. `<!DOCTYPE ...>`：这是DTD（Document Type Definition）声明，用于指定XML文档的验证规则。对于MyBatis映射文件，它需要指定MyBatis 3映射文件的DTD。
2. `<mapper>`：映射文件的根元素，包含一个`namespace`属性，用于指定映射接口的完全限定类名。映射文件中的所有SQL操作映射都应位于此元素中。

### sql标签

**这个元素可以用来定义可重用的 SQL 代码片段**，以便在其它语句中使用。 参数可以静态地（在加载的时候）确定下来，并且可以在不同的 include 元素中定义不同的参数值。比如：

```xml
<sql id="userColumns"> ${alias}.id,${alias}.username,${alias}.password </sql>
```

这个 SQL 片段可以在其它语句中使用，例如：

```xml
<select id="selectUsers" resultType="map">
  select
    <include refid="userColumns"><property name="alias" value="t1"/></include>,
    <include refid="userColumns"><property name="alias" value="t2"/></include>
  from some_table t1
    cross join some_table t2
</select>
```



### SQL映射标签

`<select>`、`<insert>`、`<update>`和`<delete>`这四个标签用于定义不同类型的SQL操作。它们有一些共同的属性，也有各自独有的属性。下面分别列出这些标签的属性及其用途。

**共同属性**：

1. `id`（必需）：指定映射语句的唯一标识符，对应Java接口中的方法名。在`<mapper>`元素内，`id`属性的值必须唯一。

2. `parameterType`（可选）：指定输入参数的Java类型。可以是完全限定类名或类型别名。如果方法参数是单个基本类型或者简单的Java对象，可以省略此属性。

3. `flushCache`（可选）：指定是否在执行此映射语句后清空一级缓存。默认值为`false`对于`<select>`，`true`对于`<insert>`、`<update>`和`<delete>`。

4. `timeout`（可选）：指定此映射语句的超时时间（以秒为单位）。如果未指定，则使用全局默认超时时间。

**`<select>`独有属性**：

1. `resultType`（可选）：指定返回结果的Java类型。可以是完全限定类名或类型别名。对于简单类型和单个Java对象，可以使用此属性。如果返回结果需要自定义映射规则，应该使用`resultMap`属性。

2. `resultMap`（可选）：指定一个自定义`<resultMap>`来处理返回结果。如果返回结果需要自定义映射规则，应该使用此属性，而不是`resultType`。

3. `fetchSize`（可选）：指定JDBC驱动程序每次获取的记录数。此属性对于处理大量数据时非常有用，因为它可以降低内存占用。不过，此属性的实际行为取决于JDBC驱动程序的实现。

4. `resultSetType`（可选）：指定`ResultSet`的类型。可选值有`FORWARD_ONLY`（只向前滚动）、`SCROLL_SENSITIVE`（可滚动，但对数据库更改敏感）和`SCROLL_INSENSITIVE`（可滚动，对数据库更改不敏感）。默认值为`undefined`，即使用JDBC驱动程序的默认设置。

5. `useCache`（可选）：指定是否启用二级缓存。默认值为`true`。

**`<insert>`独有属性**：

1. `keyProperty`（可选）：指定用于保存自动生成主键的Java对象属性。仅在使用自动生成主键的数据库时有效。

2. `keyColumn`（可选）：指定用于保存自动生成主键的数据库列。仅在使用自动生成主键的数据库时有效。

3. `useGeneratedKeys`（可选）：**指定是否使用数据库自动生成的主键。默认值为`false`。如果设置为`true`，MyBatis会尝试获取数据库生成的主键，并将其赋值给`keyProperty`指定的Java对象属性。**

4. `statementType`（可选）：指定SQL语句的类型。可选值有`PREPARED`（预编译SQL语句，默认值）、`CALLABLE`（调用存储过程）和`STATEMENT`（普通SQL语句）。

**`<update>`和`<delete>`独有属性**：

1. `statementType`（可选）：与`<insert>`标签的`statementType`属性相同，指定SQL语句的类型。可选值有`PREPARED`（预编译SQL语句，默认值）、`CALLABLE`（调用存储过程）和`STATEMENT`（普通SQL语句）。

这些属性使得MyBatis在处理各种SQL操作时具有很高的灵活性。通过为这些标签提供不同的属性值，可以调整SQL操作的行为以满足特定的需求。



### 结果映射

`resultMap` 元素是 MyBatis 中最重要最强大的元素。**它可以让你从 90% 的 JDBC `ResultSets` 数据提取代码中解放出来**，并在一些情形下允许你进行一些 JDBC 不支持的操作。实际上，在为一些比如连接的复杂语句编写映射代码的时候，一份 `resultMap` 能够代替实现同等功能的数千行代码。ResultMap 的设计思想是，对简单的语句做到零配置，对于复杂一点的语句，只需要描述语句之间的关系就行了。

对于映射类型 **如果没有指定别名的话,一般需要全路径类名**,我们可以配置type-aliases-package来指定别名,就能直接使用类名

对于这么一个对象,我们来举例resultType的使用

```
@Data
public class User {
    Long id;
    String name;
    Long age;
    String email;
}
```



#### 隐式配置

```
    <select id="getUser" resultType="com.djm.pojo.User">
        select * from user where id=#{id}
    </select>
```

这里需要User里面属性名字 与 字段名字相同(**规则映射相同,不是名字完全相同,比如字段名字是下划线分割,属性名是小驼峰**),  如果不同的话我们也可以通过设置字段别名,但是对于字段很多的话,使用又频繁的话,建议使用显示配置,我们举个设置字段别名的例子, 我们把user改成这样

```
@Data
public class User {
    Long id;
    String myName;
    Long age;
    String email;
}
```

```
    <select id="getUser" resultType="User">
        select *,name my_name from user where id=#{id}
    </select>
```



#### 显示配置

```
 <resultMap id="userResultMap" type="User">
        <result property="myName" column="name"/>
    </resultMap>
    <select id="getUser" resultMap ="userResultMap">
        select * from user where id=#{id}
    </select>
```

**其实我们也只需要配置不同的地方就行了,但是为了能够多处使用,建议写全**

resultMap里面的子配置项:

在MyBatis的`<resultMap>`元素中，可以使用以下子配置项来定义映射关系和处理复杂关系。以下是常见的子配置项及其意义：

1. `<id>`：用于指定实体类的主键属性与数据库表中的主键列之间的映射关系。`property`属性指定实体类中的属性名，`column`属性指定数据库表中的列名。

2. `<result>`：用于指定普通实体类属性与数据库表列之间的映射关系。与`<id>`类似，`property`属性指定实体类中的属性名，`column`属性指定数据库表中的列名。

3. `<association>`：用于定义一对一关系。`property`属性指定实体类中的属性名，`javaType`属性指定关联实体类的完全限定类名。`<association>`元素内部可以包含`<id>`、`<result>`、`<constructor>`等子元素来描述关联实体类的映射关系。

4. `<collection>`：用于定义一对多关系。`property`属性指定实体类中的属性名，`ofType`属性指定集合元素类型的完全限定类名。`<collection>`元素内部可以包含`<id>`、`<result>`、`<constructor>`等子元素来描述集合元素的映射关系。

5. `<constructor>`：用于指定实体类的构造方法参数与数据库表列之间的映射关系。`<constructor>`元素内部可以包含`<idArg>`和`<arg>`子元素。

   - `<idArg>`：用于指定作为构造方法参数的主键属性与数据库表中的主键列之间的映射关系。其用法类似于`<id>`。
   - `<arg>`：用于指定作为构造方法参数的普通属性与数据库表列之间的映射关系。其用法类似于`<result>`。

6. `<discriminator>`：用于实现基于数据库表列值的映射结果类型判断。`column`属性指定用于判断的数据库表列名，`javaType`属性指定该列对应的Java类型。`<discriminator>`元素内部可以包含`<case>`子元素来定义不同列值对应的映射关系。

   - `<case>`：用于定义`<discriminator>`中特定列值对应的映射关系。`value`属性指定列值，`resultType`属性指定映射结果的完全限定类名。`<case>`元素内部可以包含`<id>`、`<result>`、`<constructor>`等子元素来描述映射关系。

举个列子

```
<resultMap id="userResultMap" type="com.example.entity.User">
    <id column="user_id" property="id" />
    <result column="username" property="username" />
    <association property="profile" javaType="com.example.entity.Profile">
        <id column="profile_id" property="id" />
        <result column="email" property="email" />
        <result column="phone" property="phone" />
    </association>
    <collection property="orders" ofType="com.example.entity.Order">
        <id column="order_id" property="id" />
        <result column="order_number" property="orderNumber" />
    </collection>
</resultMap>

```



### 动态SQL

动态SQL是MyBatis中的一种功能，它使你能够根据参数、条件等动态地构建和修改SQL语句。动态SQL提高了代码的可读性和灵活性，尤其在处理复杂查询、条件过滤和分页等场景时非常有用。

以下是MyBatis中常用的动态SQL元素及其用途：

1. `<if>`：条件判断，只有当条件成立时，才会包含`<if>`元素内的SQL片段。
   示例：
   ```
   <select id="findUsers" resultType="User">
     SELECT * FROM users
     <where>
       <if test="username != null">
         AND username = #{username}
       </if>
       <if test="email != null">
         AND email = #{email}
       </if>
     </where>
   </select>
   ```
   当`username`和`email`参数不为`null`时，相应的条件将被包含在查询语句中。

2. `<choose>`、`<when>`和`<otherwise>`：类似于Java的`switch`语句，用于根据条件选择不同的SQL片段。
   示例：
   ```
   <select id="findUsers" resultType="User">
     SELECT * FROM users
     <where>
       <choose>
         <when test="username != null">
           username = #{username}
         </when>
         <when test="email != null">
           email = #{email}
         </when>
         <otherwise>
           id = #{id}
         </otherwise>
       </choose>
     </where>
   </select>
   ```
   当`username`不为`null`时，查询将根据`username`进行；当`username`为`null`且`email`不为`null`时，查询将根据`email`进行；否则，查询将根据`id`进行。

3. `<where>`：用于生成`WHERE`子句，可以包含动态元素。它会自动处理开头的`AND`或`OR`关键字。
   示例：
   ```
   <select id="findUsers" resultType="User">
     SELECT * FROM users
     <where>
       <if test="username != null">
         username = #{username}
       </if>
       <if test="email != null">
         AND email = #{email}
       </if>
     </where>
   </select>
   ```
   `<where>`元素会自动处理开头的`AND`关键字，生成有效的SQL语句。

4. `<set>`：用于生成`SET`子句，常用于`UPDATE`语句。它会自动处理结尾的逗号。
   示例：
   ```
   <update id="updateUser" parameterType="User">
     UPDATE users
     <set>
       <if test="username != null">
         username = #{username},
       </if>
       <if test="email != null">
         email = #{email},
       </if>
     </set>
     WHERE id = #{id}
   </update>
   ```
   `<set>`元素会自动处理结尾的逗号，生成有效的SQL语句。

5. `<foreach>`：用于遍历集合或数组，并对每个元素执行相同的SQL片段。`<foreach>`元素可以生成`IN`子句，或用于批量插入、更新、删除操作。示例：

      ```
      <select id="findUsersByIds" resultType="User">
        SELECT * FROM users
        WHERE id IN
        <foreach item="id" index="index" collection="ids" open="(" separator="," close=")">
          #{id}
        </foreach>
      </select>
      ```
   当`ids`参数为一个包含多个`id`值的集合时，`<foreach>`元素会生成一个`IN`子句，查询所有匹配的用户。

6. `<trim>`：用于自定义SQL片段的前缀、后缀、前缀覆盖和后缀覆盖。`<trim>`元素内可以包含动态元素，如`<if>`。`<trim>`元素提供了比`<where>`和`<set>`更高的灵活性。 示例：

   ```
   bashCopy code<update id="updateUser" parameterType="User">
     UPDATE users
     <trim prefix="SET" suffixOverrides=",">
       <if test="username != null">
         username = #{username},
       </if>
       <if test="email != null">
         email = #{email},
       </if>
     </trim>
     WHERE id = #{id}
   </update>
   ```

   `<trim>`元素会根据指定的前缀和后缀覆盖规则生成SQL片段，使得SQL语句更加灵活。

7. `<bind>`：用于创建一个变量，并将其绑定到指定的表达式。`<bind>`元素可以用于计算中间结果，或在多个地方重复使用相同的表达式。 示例：

   ```
   bashCopy code<select id="findUsers" resultType="User">
     <bind name="pattern" value="'%' + username + '%'"/>
     SELECT * FROM users
     <where>
       <if test="username != null">
         username LIKE #{pattern}
       </if>
     </where>
   </select>
   ```

   `<bind>`元素创建了一个名为`pattern`的变量，将其绑定到一个包含通配符的表达式，用于模糊查询。

通过组合使用这些动态SQL元素，你可以根据不同的条件和参数值生成灵活、可维护的SQL语句。动态SQL在处理复杂查询、条件过滤和分页等场景时非常有用。

### $ 与# #

在MyBatis中，`$`和`#`都用于在SQL语句中插入参数值，但它们的用途和行为有所不同。

1. `#{}`：使用`#`括起来的参数表示预编译参数。MyBatis会将这些参数值作为预编译语句的参数进行传递，这样可以避免SQL注入的风险。此外，MyBatis会根据参数类型自动进行类型处理，例如将Java中的`Date`类型转换为数据库中的`TIMESTAMP`类型。

   示例：
   ```
   SELECT * FROM users WHERE username = #{username}
   ```
   当`username`参数为`'admin'`时，生成的SQL语句如下：
   ```
   SELECT * FROM users WHERE username = ?
   ```
   在执行SQL语句时，MyBatis会将`'admin'`作为预编译参数传递给数据库。

2. `${}`：使用`$`括起来的参数表示直接插入参数值。MyBatis会将这些参数值直接替换到SQL语句中，而不会进行预编译。这样做可能会导致SQL注入的风险。因此，你应该谨慎使用`$`，尽量避免在可控制的参数上使用它。`$`通常用于动态表名、列名等无法通过预编译参数实现的场景。

   示例：
   ```
   SELECT * FROM users ORDER BY ${columnName} ${order}
   ```
   当`columnName`参数为`'username'`，`order`参数为`'ASC'`时，生成的SQL语句如下：
   ```
   SELECT * FROM users ORDER BY username ASC
   ```

总结：
- `#{}`：用于预编译参数，安全且支持类型处理。
- `${}`：用于直接插入参数值，可能导致SQL注入，谨慎使用。

在大多数情况下，你应该优先使用`#{}`作为参数占位符，以保证安全和正确的类型处理。只有在必要的时候，如动态表名、列名等，才考虑使用`${}`。

## Mapper位置扫描

在Spring Boot应用中，`@MapperScan`注解和配置文件中的`mybatis.mapper-locations`配置都可以用于指定MyBatis的mapper接口和XML映射文件的位置。**这两者是互补的，它们会合并而不是替换**。这意味着，如果您在`@MapperScan`注解中指定了一个包路径，并且在配置文件中也指定了一个或多个文件路径，那么MyBatis将会扫描这些路径，加载所有符合条件的mapper接口和XML映射文件。



## 配置项

```java
    private String configLocation;  //MyBatis 配置文件（如：mybatis-config.xml）的位置,一般不用
    private String[] mapperLocations = new String[]{"classpath*:/mapper/**/*.xml"}; //XML 映射文件的位置，可以使用通配符来指定多个文件
    private String typeAliasesPackage; // 别名包，用于为实体类自动创建别名
    private Class<?> typeAliasesSuperType; //为继承自某个类的子类创建别名
    private String typeHandlersPackage;  // 类型处理器包，用于指定自定义类型处理器所在的包
    private boolean checkConfigLocation = false; // 是否检查配置文件的存在。如果设置为 true，则会在找不到配置文件时抛出异常。
    private ExecutorType executorType;  // MyBatis 的执行器类型（如：SIMPLE、REUSE、BATCH）
    private Class<? extends LanguageDriver> defaultScriptingLanguageDriver;  // 默认的脚本语言驱动
    private Properties configurationProperties; // 自定义配置项。
    @NestedConfigurationProperty
    private MybatisConfiguration configuration;  //MyBatis 的配置，可以用来配置一些 MyBatis 原生的特性。
		   protected final MybatisMapperRegistry mybatisMapperRegistry; // MyBatis 映射器注册表
            protected final Map<String, Cache> caches; //MyBatis 缓存对象的映射
            protected final Map<String, ResultMap> resultMaps; // 结果映射的映射
            protected final Map<String, ParameterMap> parameterMaps; 
            protected final Map<String, KeyGenerator> keyGenerators;
            protected final Map<String, XNode> sqlFragments;
            protected final Map<String, MappedStatement> mappedStatements; //映射语句的映射
            private boolean useGeneratedShortKey; //是否使用自动生成的短键名
    /** @deprecated */
    @Deprecated
    private String typeEnumsPackage; // 枚举类型的包名（已弃用）
    @NestedConfigurationProperty
    private GlobalConfig globalConfig = GlobalConfigUtils.defaults()
        private boolean banner = true;  //是否在启动时显示 MyBatis-Plus 的 Banner 信息，默认为 true
        private boolean enableSqlRunner = false; //是否启用 SQL 运行器，它允许在项目启动后直接运行 SQL，而无需编写映射器和服务类，默认为 false
        private GlobalConfig.DbConfig dbConfig;  //MyBatis-Plus 的数据库配置，用于配置数据库相关的参数
			   private IdType idType; //主键类型，用于配置实体类的主键生成策略（如：AUTO、INPUT、UUID 等）。
                private String tablePrefix; // 表前缀，用于自动映射实体类和数据库表之间的关系
                private String schema; // 数据库 schema，用于指定查询时的默认 schema
                private String columnFormat; //列名格式化，用于自定义数据库列名的格式
                private String propertyFormat; // 属性名格式化，用于自定义实体类属性名的格式
                private boolean replacePlaceholder; // 是否替换占位符，默认为 false。
                private String escapeSymbol; // 转义符，用于在 SQL 中转义特殊字符。
                private boolean tableUnderline; //是否使用表名下划线分隔，默认为 true。
                private boolean capitalMode;  // 是否使用大写命名，默认为 false。
                private List<IKeyGenerator> keyGenerators; 
                private String logicDeleteField;
                private String logicDeleteValue;
                private String logicNotDeleteValue;
                private FieldStrategy insertStrategy;
                private FieldStrategy updateStrategy;
                /** @deprecated */
                @Deprecated
                private FieldStrategy selectStrategy;
                private FieldStrategy whereStrategy;
			
        private ISqlInjector sqlInjector = new DefaultSqlInjector(); //SQL 注入器，用于向 MyBatis-Plus 添加自定义的 SQL 方法，默认为 DefaultSqlInjector
        private Class<?> superMapperClass = Mapper.class; // Mapper 接口的超类，所有的 Mapper 接口都应继承这个超类，默认为 Mapper.class。
        private SqlSessionFactory sqlSessionFactory; //MyBatis 的 SqlSessionFactory 实例，用于创建 SqlSession。
        private Set<String> mapperRegistryCache = new ConcurrentSkipListSet(); //映射器注册缓存，存储已注册的 Mapper 接口。
        private MetaObjectHandler metaObjectHandler; // 元对象处理器，用于自动填充实体类中的字段。
        private PostInitTableInfoHandler postInitTableInfoHandler = new PostInitTableInfoHandler() {
        }; //表信息初始化后的处理器，允许您在表信息初始化后自定义一些操作。
        private IdentifierGenerator identifierGenerator; //标识符生成器，用于自定义实体类的主键生成策略
        
```



# Spring Security 

## 基础的安全概念

在计算机安全中，主要涉及到两个基本概念：身份验证(Authentication)和授权(Authorization)。

1. **身份验证(Authentication)**：身份验证是确认用户身份的过程，通常涉及用户名和密码，但也可能包括更复杂的过程，如两步验证和数字证书。当用户首次访问系统时，他们会被要求提供凭证，如用户名和密码，系统将根据这些凭证确认用户的身份。在 Spring Security 中，身份验证过程由 AuthenticationManager 接口管理。

2. **授权(Authorization)**：一旦用户的身份得到确认，下一步就是确定他们可以访问系统的哪些资源，以及他们可以执行哪些操作，这就是授权过程。例如，一个用户可能被授权读取一个文件，但不能删除它。另一个用户可能被授权修改该文件，但不能查看它。在 Spring Security 中，授权过程由 AccessDecisionManager 接口管理。

理解这两个概念是学习 Spring Security 的基础。在应用程序中，我们需要根据用户的角色和权限对资源进行保护，只有经过正确的身份验证和授权的用户才能访问这些资源。在接下来的学习中，我们将更深入地探讨这两个概念，并学习如何在 Spring Security 中实现身份验证和授权。

## 基本定义

Spring Security 是一个用于为 Java 应用程序提供身份验证和授权功能的安全框架。在 Spring Boot 中，Spring Security 可以轻松集成，提供自动配置和默认安全设置。以下是 Spring Security 在 Spring Boot 应用中的工作机制和工作流程：

1. 配置和启动：当 Spring Boot 检测到 Spring Security 在 classpath 中时，它会自动启用 Spring Security，并提供基本的安全配置。你可以通过在配置文件中添加自定义配置或创建自定义的 `WebSecurityConfigurerAdapter` 类来覆盖默认配置。

2. 过滤器链：Spring Security 在应用中使用 Servlet 过滤器链来处理 HTTP 请求。过滤器链中包含多个过滤器，负责处理不同的安全功能，如身份验证、授权、跨站请求伪造保护（CSRF）等。当一个请求到达应用时，它首先经过过滤器链的处理。

3. 身份验证：在过滤器链中，`UsernamePasswordAuthenticationFilter` 负责处理基于表单的登录请求。**这个过滤器会尝试从请求中提取用户名和密码**，然后将它们封装成一个 `Authentication` 对象。接着，`AuthenticationManager` 负责处理这个 `Authentication` 对象，将其传递给相应的 `AuthenticationProvider`，如 `DaoAuthenticationProvider`。`AuthenticationProvider` 会调用 `UserDetailsService` 来加载用户的详细信息（如密码、角色等），并将其与请求中提供的凭据进行比较。如果凭据匹配，`AuthenticationProvider` 会返回一个已认证的 `Authentication` 对象，包含用户的详细信息和授权。

4. 授权：Spring Security 使用 `AccessDecisionManager` 来处理授权决策。当一个已认证的请求尝试访问受保护的资源时，`AccessDecisionManager` 会检查用户的授权（如角色、权限等）是否允许访问该资源。如果用户具有相应的授权，请求将被允许访问资源；否则，将返回一个 HTTP 403（Forbidden）响应。

5. 异常处理：Spring Security 使用 `AuthenticationEntryPoint` 和 `AccessDeniedHandler` 来处理身份验证和授权异常。例如，当未认证的用户尝试访问受保护资源时，`AuthenticationEntryPoint` 会返回一个 HTTP 401（Unauthorized）响应，通常会引导用户登录。当已认证的用户尝试访问不具有权限的资源时，`AccessDeniedHandler` 会返回一个 HTTP 403（Forbidden）响应。

6. 会话管理：Spring Security 提供了会话管理功能，包括创建新会话、超时设置和并发控制等。此外，Spring Security 支持持久化会话数据，以便在应用重启后还能保持会话状态。

7. 注销：Spring Security 提供了注销功能，允许用户安全地结束会话并清除相关的认证信息。默认情况下，用户可以通过访问 `/logout` URL 发起注销请求。`LogoutFilter` 负责处理这些请求，并调用配置的 `LogoutHandler` 实现来执行注销操作，如清除安全上下文、使当前会话失效、删除持久化的会话数据等。注销完成后，可以将用户重定向到指定的 URL，通常是登录页面或主页。

8. 记住我：Spring Security 支持“记住我”功能，允许用户在关闭浏览器或会话过期后仍然保持登录状态。该功能通过在用户浏览器中设置一个特殊的 cookie 来实现。在接收到请求时，`RememberMeAuthenticationFilter` 会检查这个 cookie，如果存在并有效，它会自动为用户创建一个已认证的安全上下文，无需重新登录。你可以在配置中启用和自定义“记住我”功能，例如设置 cookie 的有效期、加密密钥等。

9. 跨站请求伪造（CSRF）保护：Spring Security 提供了 CSRF 保护功能，可以防止恶意网站伪造用户的请求。默认情况下，Spring Security 会为所有的 POST、PUT、DELETE 等非幂等请求启用 CSRF 保护。要实现这个功能，`CsrfFilter` 会在每个请求中查找一个名为 `_csrf` 的 token（通常以参数或 HTTP 头的形式传递），并将其与服务器端存储的 token 进行比较。如果 token 不存在或不匹配，请求将被拒绝。开发者需要在表单提交和 AJAX 请求中正确携带 CSRF token，以确保请求能够通过验证。

10. 跨域资源共享（CORS）配置：Spring Security 支持 CORS 配置，允许在不同域名之间进行安全的资源共享。你可以通过 `WebSecurityConfigurerAdapter` 定义全局或特定的 CORS 策略，例如允许的源、请求方法、头部等。

11. 自定义扩展：Spring Security 提供了许多扩展点，允许开发者根据需求定制安全功能。例如，你可以实现自定义的 `UserDetailsService`、`AuthenticationProvider`、`AccessDecisionVoter` 等，以支持特定的认证和授权策略。此外，Spring Security 支持 OAuth2、OpenID Connect、SAML 等多种身份验证和单点登录（SSO）协议，可以通过添加相应的依赖和配置来集成这些协议。



## 核心组件

Spring Security 是一个功能强大且可高度自定义的身份验证和访问控制框架。以下是其主要的核心接口和组件：

1. `Authentication`：这是一个接口，保存了主体的详细信息。当用户成功登录后，所有的详细信息都会被存储在这个对象中。

2. `AuthenticationManager`：这是一个接口，它定义了一个方法 `authenticate()`，该方法可以从任何位置调用以进行身份验证。

3. `ProviderManager`：这是 AuthenticationManager 的一个实现。它迭代通过 ProviderManager 配置的 AuthenticationProvider 列表。

4. `AuthenticationProvider`：这是一个接口，它的实现提供了一个方式来获取用户详细信息。

5. `UserDetailsService`：这是一个接口，它定义了一个方法 `loadUserByUsername()`。这个方法在任何位置都可以调用，以获取用户详细信息。

6. `GrantedAuthority`：这是一个接口，代表应用程序的认证对象的授权，即角色和权限。

7. `SecurityContextHolder`：这是一个类，它用于存储当前线程的安全上下文，包括当前用户的详细信息。

8. `SecurityContext`：这是一个接口，用于保存 Authentication 和可能的任何其他需要的信息。

9. `AccessDecisionManager`：这是一个接口，用于做访问控制决策。

10. `FilterSecurityInterceptor`：这是一个类，它处理所有 HTTP 请求并检查安全性。它是 Spring Security Web 安全的核心组件。

以上就是 Spring Security 中的一些主要接口和组件。要注意的是，Spring Security 的设计是可插拔的，这意味着这些接口和组件可以根据需要进行自定义和替换。

## 核心过滤器

在Spring Security 5中，有16个主要的过滤器，它们按照执行顺序如下：

1. `ChannelProcessingFilter`：处理请求的安全通道，例如http与https。

2. `SecurityContextPersistenceFilter`：在`HttpSession`中存储并提取`SecurityContext`，在每个请求上下文中保持用户身份。

3. `ConcurrentSessionFilter`：在用户登录时检查并限制同时登录的会话数量。

4. `HeaderWriterFilter`：向HTTP响应中添加安全头，如X-XSS-Protection，X-Content-Type-Options。

5. `CsrfFilter`：**提供跨站请求伪造（CSRF）保护，验证请求中的CSRF token**。

6. `LogoutFilter`：处理用户的注销，清除用户的认证信息和会话。

7. `UsernamePasswordAuthenticationFilter`：处理基于表单的认证请求，即用户名和密码的认证。

8. `DefaultLoginPageGeneratingFilter`：如果应用没有定义登录页面，这个过滤器将生成一个默认的登录页面。

9. `DefaultLogoutPageGeneratingFilter`：如果应用没有定义注销页面，这个过滤器将生成一个默认的注销页面。

10. `BasicAuthenticationFilter`：处理HTTP Basic认证请求。

11. `RequestCacheAwareFilter`：检查并使用缓存的请求，例如在登录前访问的受保护资源。

12. `SecurityContextHolderAwareRequestFilter`：向请求中添加安全上下文凭据，如用户身份。

13. `AnonymousAuthenticationFilter`：为未认证的用户创建一个匿名的`Authentication`，使你能够对未认证的用户进行授权决策。

14. `SessionManagementFilter`：处理会话管理，包括固定会话保护和并发会话控制。

15. `ExceptionTranslationFilter`：捕获Spring Security引发的异常并启动认证流程或发送HTTP 403状态码。

16. `FilterSecurityInterceptor`：最后的过滤器，它根据用户的认证信息和访问的URL，决定用户是否有权限访问该资源。

这是Spring Security的默认过滤器链，但你可以根据你的需求对其进行定制和扩展。

这样过滤器最终都会被执行他们就像函数递归一样, 先自己做一点事情  然后开始递归下去, 等到递归完毕后  自己再做一点事情, 这些过滤器最主要的就是做三件事,  认证, 授权, 保护 



## 鉴权

spring sercurity给我们提供了权限校验的功能, 对于那些需要权限的接口, 它会去检测用户的凭证信息, 查看它是否具有这个权限访问这个接口, 鉴权可以在配置类中声明,也可以在方法上声明

配置类中声明

```
 httpSecurity.authorizeRequests()
                .antMatchers("/hello").hasAuthority("admin") // 这个接口需要admin权限
                .antMatchers("/test1").hasAuthority("p1") // 这个接口需要p1权限
```

方法上声明

```
// 开启方法注解支持
@Configuration
@EnableWebSecurity
@EnableMethodSecurity
public class SecurityConfig 
```

```
   @RequestMapping("/hello")
    @PreAuthorize("hasAuthority('admin')")
    public String login() {
        return "hello world";
    }
```

## 失败处理

### 认证失败处理

```java
public class MyUnauthorizedHandler implements AuthenticationEntryPoint {
    @Override
    public void commence(HttpServletRequest request, HttpServletResponse response, AuthenticationException authException) throws IOException, ServletException {
        response.setCharacterEncoding("UTF-8");
        response.setContentType("application/json");
        response.getWriter().println("认证失败");
        response.getWriter().flush();
    }
}

```

配置类里面修改

```java
 httpSecurity.exceptionHandling().authenticationEntryPoint(new MyUnauthorizedHandler()); // 添加自定义的未认证处理
```

### 鉴权失败处理

```java
public class MyAccessDeniedHandler implements AccessDeniedHandler {
    @Override
    public void handle(HttpServletRequest request, HttpServletResponse response, AccessDeniedException accessDeniedException) throws IOException, ServletException {
        response.setCharacterEncoding("UTF-8");
        response.setContentType("application/json");
        response.getWriter().println("没有权限访问");
        response.getWriter().flush();
    }
}
```

配置类里面修改

```java
 httpSecurity.exceptionHandling().accessDeniedHandler(new MyAccessDeniedHandler()); // 添加自定义的未授权处理器
```

## 自定义认证

spring Security 的自定义实际上涵盖了三个主要的部分：

1. **用户信息的获取**：这个部分是关于如何从请求中提取用户的身份信息。例如，这可能包含从请求头中提取一个token，或者从请求参数或体中提取用户名和密码。你需要自定义一个部分来告诉 Spring Security 如何获取这些信息。这一部分需要自定义过滤器去处理

2. **认证过程**：这个部分描述了验证用户身份的过程。你需要自定义一个认证处理器，告诉 Spring Security 如何根据提供的信息判断用户的身份是否有效。这可能涉及到与数据库的交互，或者与第三方身份验证服务的交互。这一部分可以用AuthenticationProvider去处理,也可以在过滤器中处理

3. **用户信息的加载与比对**：这个部分是指定如何从你的数据源（例如数据库或者其他服务）加载用户的详细信息，并与获取到的用户信息进行比对。你需要自定义一个“用户详情服务”，来告诉 Spring Security 如何加载用户数据并进行比对。可以用UserDetailsService,也可以自己用其他方法拿到用户存好的信息

这三个步骤构成了自定义 Spring Security 的基础框架。通过这样的设计，Spring Security 能够在一个统一的框架内处理各种各样的身份验证方法，同时还能够保持很高的灵活性，适应各种复杂的需求场景。

## 自定义token认证

### 创建身份信息

```
public class JwtAuthenticationToken extends AbstractAuthenticationToken {


    private String token;

    public JwtAuthenticationToken(String token) {
        super(null);
        this.token = token;
    }

    public JwtAuthenticationToken(Collection<? extends GrantedAuthority> authorities) {
        super(authorities);
        setAuthenticated(true);
    }


    @Override
    public Object getCredentials() {
        return null;
    }

    @Override
    public Object getPrincipal() {
        return null;
    }

    public String getToken() {
        return token;
    }
}
```

### 创建验证器

```
public class JwtAuthenticationProvider implements AuthenticationProvider {



    @Override
    public Authentication authenticate(Authentication authentication) throws AuthenticationException {
        JwtAuthenticationToken jwtAuthenticationToken = (JwtAuthenticationToken) authentication;

        if(!TokenUtil.isOk(jwtAuthenticationToken.getToken())){
            return jwtAuthenticationToken; // 验证失败,直接返回未验证的信息,如果后面还有过滤器的话,交给他们看他们能不能处理
        }
        
        // 验证成功,设置为已验证
        jwtAuthenticationToken.setAuthenticated(true);
        JSONObject map =  TokenUtil.parseToken(jwtAuthenticationToken.getToken());

        List<String> stringList = map.getBeanList("authorities", String.class);

        stringList.forEach(System.out::println);

        List<SimpleGrantedAuthority> authorities = new LinkedList<>();
        stringList.forEach(s -> authorities.add(new SimpleGrantedAuthority(s)));
        // 生成一个已验证的JwtAuthenticationToken,并把authorities和map设置进去
        JwtAuthenticationToken jwtAuthenticationToken1 = new JwtAuthenticationToken(authorities);
        jwtAuthenticationToken1.setDetails(map);
        return jwtAuthenticationToken1;

    }

    @Override
    public boolean supports(Class<?> authentication) {
        // 判断传进来的authentication是不是JwtAuthenticationToken的子类,如果是就返回true,表示支持
        return authentication.isAssignableFrom(JwtAuthenticationToken.class);
    }
}
```

#### 创建过滤器

```
public class JwtAuthenticationTokenFilter extends OncePerRequestFilter {

    public static String HEADER = "Authorization";
    public static String TYPE = "Bearer ";

    @Autowired
    private AuthenticationManager authenticationManager;


    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {

        String header = request.getHeader(HEADER);
        if(header != null && header.startsWith(TYPE)){
            String token = header.substring(TYPE.length());

            JwtAuthenticationToken jwtAuthenticationToken = new JwtAuthenticationToken(token);
            Authentication authenticate = authenticationManager.authenticate(jwtAuthenticationToken);
            if(authenticate != null && authenticate.isAuthenticated()){
                SecurityContextHolder.getContext().setAuthentication(authenticate);
            }
        }

        filterChain.doFilter(request,response);
    }


}

```

### 自定义登录请求

```
@RestController
public class UserController {

    @Autowired
    private UserService userService;

    @PostMapping("/login")
    public Map<String,Object> login(@RequestBody Map<String,Object> map){
        String username = (String) map.get("username");
        String password = (String) map.get("password");

        User user = userService.getUserByUsername(username);

        if(user == null) {
            return Map.of("code",200,"msg","用户不存在");
        }

        if(!user.getPassword().equals(password)) {
            return Map.of("code",200,"msg","密码错误");
        }

        LinkedHashMap<String, Object> data = new LinkedHashMap<>();
        data.put("id", user.getId());
        data.put("username", user.getUsername());

        data.put("authorities", user.getRoles());

        String token = "Bearer " + TokenUtil.getToken(data);



        return Map.of("code",200,"msg","登录成功","token",token);

    }

    @RequestMapping("/logout")
    public Map<String,Object> logout() {

        // 拿到当前的SecurityContext
        SecurityContext context = SecurityContextHolder.getContext();

        // 拿到当前的Authentication
        Authentication authentication = context.getAuthentication();

        // 如果是匿名用户，就直接返回没有登录
        if(authentication.getClass().isAssignableFrom(AnonymousAuthenticationToken.class)) {
           return Map.of("code",200,"msg","用户未登录");
        }

        // 如果是已经登录的用户，就清空SecurityContextHolder中的信息
        SecurityContextHolder.clearContext();
        return Map.of("code",200,"msg","登出成功");
    }

}

```

### 配置类

```
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Autowired
    AuthenticationConfiguration authenticationConfiguration;

    @Bean
    public JwtAuthenticationProvider jwtAuthenticationProvider(){
        return new JwtAuthenticationProvider();
    }

    @Bean
    public AuthenticationManager authenticationManager() throws Exception {
        return authenticationConfiguration.getAuthenticationManager();
    }


    @Bean
    public JwtAuthenticationTokenFilter jwtAuthenticationTokenFilter() throws Exception {
        return new JwtAuthenticationTokenFilter();

    }

    @Bean
    public SecurityFilterChain defaultSecurityFilterChain(HttpSecurity httpSecurity) throws Exception {

        httpSecurity.authorizeRequests()
                .antMatchers("/hello").hasAuthority("admin") // 这个接口需要p1权限
                .antMatchers("/login","/logout").permitAll() // 这两个接口不需要认证
                .antMatchers("/test1").hasAuthority("p1") // 这个接口不需要认证，但是不能是已经认证的用户
                .anyRequest().authenticated() // 其他接口都需要认证
                .and()
                .formLogin().disable()  // 禁用默认表单登录
                .logout().disable() // 禁用默认退出登录
                .csrf().disable() // 禁用csrf
                .sessionManagement().disable(); // 禁用session
        // 添加自定义的jwt认证器
        httpSecurity.authenticationProvider(jwtAuthenticationProvider());

        // 添加自定义的jwt过滤器
        httpSecurity.addFilterBefore(jwtAuthenticationTokenFilter(), UsernamePasswordAuthenticationFilter.class);
        httpSecurity.authenticationManager(authenticationConfiguration.getAuthenticationManager());
        return httpSecurity.build();
    }

}

```

这个是按照标准的三步走, 但是我感觉有点麻烦, 我其实可以在filter里面全部弄完,不需要验证器, 这样多方便



## 补充

### 过滤链

在Spring Security的过滤器链中，每个过滤器会依次处理请求。**一旦一个过滤器完成了身份验证，它会填充Security Context，后续的过滤器通常就会跳过身份验证步骤**。**如果一个过滤器没有完成身份验证，那么请求就会继续传递给后续的过滤器进行处理**。前提是这个过程没有抛出异常

所以，如果 `UsernamePasswordAuthenticationFilter` 没有完成身份验证（例如，请求中没有包含用户名和密码），那么你的自定义过滤器就有机会处理这个请求。

这就是为什么过滤器的顺序很重要。如果你希望自定义的过滤器能处理特定类型的身份验证，那么你需要确保它位于能处理这种类型身份验证的内置过滤器之前。这样，当内置过滤器不能处理请求时，你的自定义过滤器就可以接手处理。

这种设计让Spring Security能够支持多种类型的身份验证，并且可以通过添加自定义过滤器来扩展其功能。

### AuthenticationProvider优先级

Spring Security 的 `ProviderManager`（`AuthenticationManager` 的一个实现）会遍历所有的 `AuthenticationProvider` 实例，按照它们在配置中的顺序，依次尝试对提供的 `Authentication` 对象进行认证。

当 `ProviderManager` 找到一个能够处理当前 `Authentication` 对象的 `AuthenticationProvider` 时，它会调用这个 `AuthenticationProvider` 的 `authenticate` 方法。如果该 `AuthenticationProvider` **认证成功，则认证过程结束**，否则，`ProviderManager` 会继续尝试下一个 `AuthenticationProvider`。

如果所有的 `AuthenticationProvider` 都无法认证成功，`ProviderManager` 会抛出一个 `AuthenticationException`。

因此，你可以根据你的需求配置多个 `AuthenticationProvider`，Spring Security 会按照它们在配置中的顺序，依次尝试每个 `AuthenticationProvider`。并且，你可以为每种 `Authentication` 类型（如用户名密码、OAuth 2.0 token、LDAP 等）配置不同的 `AuthenticationProvider`。

### hasRole 和 hasAuthority的区别

在 Spring Security 中，`hasAuthority()` 和 `hasRole()` 都是方法级别的安全性注解，用于决定某个用户是否拥有访问特定方法的权限。但是它们之间存在一些细微的差别：

1. **hasAuthority()**: 这个方法会检查 `Authentication` 对象中的 `GrantedAuthority` 列表，看用户是否具有指定的权限。你可以使用任意的字符串来作为权限，例如 `hasAuthority('READ')`。

2. **hasRole()**: 这个方法也会检查 `Authentication` 对象中的 `GrantedAuthority` 列表，但它假定你的权限是以 `ROLE_` 前缀开头的。所以，如果你有一个名为 `ROLE_ADMIN` 的权限，你可以使用 `hasRole('ADMIN')` 来检查用户是否拥有这个权限。也就是说，`hasRole()` 会自动在你给定的角色名前加上 `ROLE_` 前缀。

总的来说，`hasAuthority()` 和 `hasRole()` 的功能基本相同，但是 `hasRole()` 更适用于检查以 `ROLE_` 前缀命名的权限，而 `hasAuthority()` 可以用来检查任何名称的权限。你可以根据你的实际需求来选择使用哪个方法。

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







# 日志

## 日志门面和日志实现

![image-20230430143718193](../../img/spring系列assets/image-20230430143718193.png)



JUL是jdk自带，在java.util.logging包下的Logger类

Log4j是Apache下的一款开源的日志框架

**Logback是由log4j创始人设计的另一个开源日志组件，性能比log4j要好**

Log4j 2是对Log4j的升级版，参考了logback的一些优秀的设计

Log4j2主要有以下特色:

性能提升：Log4j 2包含基于LMAX Disruptor库的下一代**异步记录器**。在多线程方案中，与Log4j 1.x和Logback相比，异步Logger的吞吐量高18倍，延迟降低了几个数量级

自动重载配置：与Logback一样，Log4j 2可以在修改后自动重新加载其配置。与Logback不同，它在进行重新配置时不会丢失日志事件

无垃圾机制：在稳态日志记录期间，Log4j 2 在独立应用程序中是无垃圾的，而在Web应用程序中是低垃圾的。这样可以减少垃圾收集器上的压力，并可以提供更好的响应时间性能

## 使用日志框架

Spring Boot内置了对日志的支持，它为开发者提供了一个统一、易于配置的日志框架。默认情况下，**Spring Boot使用Logback作为其日志实现**。然而，它也提供了对其他日志框架（如Log4j2）的支持，可以通过简单的配置进行切换。

日志级别：
Spring Boot支持以下日志级别，按照日志输出的详细程度递减排列：

1. ERROR：错误级别，仅记录错误信息。
2. WARN：警告级别，记录警告和错误信息。
3. INFO：信息级别，记录信息、警告和错误信息。**这是Spring Boot的默认日志级别**。
4. DEBUG：调试级别，记录调试、信息、警告和错误信息。比INFO级别的日志更详细。
5. TRACE：追踪级别，记录所有日志信息，包括追踪、调试、信息、警告和错误信息。这是最详细的日志级别。

### 方式一

为了在你的应用程序中使用日志，你需要导入适当的日志API。对于Spring Boot，默认情况下，**你应该使用SLF4J（Simple Logging Facade for Java）API**。首先，在你的Java类中导入以下包：

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
```

然后，创建一个`Logger`实例：

```java
private static final Logger logger = LoggerFactory.getLogger(YourClassName.class);
```

现在，你可以使用`logger`实例记录不同级别的日志：

```java
logger.error("这是一条错误日志");
logger.warn("这是一条警告日志");
logger.info("这是一条信息日志");
logger.debug("这是一条调试日志");
logger.trace("这是一条追踪日志");
```

### 方式二

使用lombok注解,自动帮我们生成一个log对象

```java
@Component
@Log
@Slf4j
public class MyHttpSessionEventListener implements HttpSessionListener {

    @Override
    public void sessionCreated(HttpSessionEvent se) {

        log.info("session创建: " + se.getSession().getId());
        System.out.println("session创建: " + se.getSession().getId());
    }

    @Override
    public void sessionDestroyed(HttpSessionEvent se) {
        System.out.println("session销毁: " + se.getSession().getId());
    }
}

```



## 日志配置

Spring Boot允许你通过`application.properties`或`application.yml`文件轻松地配置日志。以下是一些常见的日志配置选项：

- 日志级别配置：通过`logging.level`属性设置包或类的日志级别。例如：

  ```properties
  logging.level.root=WARN
  logging.level.com.example.demo=DEBUG
  ```

- 日志文件配置：通过`logging.file.name`或`logging.file.path`属性设置日志输出文件。例如：

  ```properties
  logging.file.name=myapp.log
  logging.file.path=logs
  ```

- 日志文件的滚动策略、最大文件大小等配置：在Logback或Log4j2的配置文件中设置。例如，在`src/main/resources`目录下创建一个名为`logback-spring.xml`的文件，然后自定义相关配置。

### 配置文件

Spring Boot 在启动时会自动检测项目 `src/main/resources` 目录下的一些特定命名的配置文件，并根据这些文件的名称来确定它们的用途。对于日志配置，Spring Boot 会检查以下文件名：

- Logback：`logback-spring.xml`、`logback.xml`
- Log4j2：`log4j2-spring.xml`、`log4j2.xml`

当 Spring Boot 找到这些文件中的一个时，它会自动将其用作日志系统的配置。在这些文件中，你可以使用相应日志框架的语法和配置元素来定制日志系统的行为。

请注意，对于 Logback，推荐使用 `logback-spring.xml` 而不是 `logback.xml`。使用 `logback-spring.xml` 文件名，你可以利用 Spring Boot 提供的一些额外特性，例如使用 Spring Profile 进行条件化配置。而使用 `logback.xml`，这些特性将不可用。

总之，Spring Boot 通过检测特定的文件名来识别日志配置文件，并在启动过程中自动应用这些配置。



```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <include resource="org/springframework/boot/logging/logback/base.xml" />

    <!-- 设置日志级别 -->
    <logger name="com.example.demo" level="DEBUG" />

    <!-- 控制台日志输出 -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <!-- 文件日志输出 -->
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/app.log</file>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <!-- 设置滚动策略 -->
            <fileNamePattern>logs/app-%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
    </appender>

    <!-- 将输出引用到控制台和文件日志,这个是兜底的,如果前面设置了其他的级别,会使用那个级别 -->
    <root level="INFO">
        <appender-ref ref="CONSOLE" />
        <appender-ref ref="FILE" />
    </root>
</configuration>

```

滚动策略是用于管理日志文件的生成和清理的一种策略。当日志文件的大小或时间达到一定阈值时，滚动策略会自动将当前日志文件“滚动”为一个新的日志文件。这样可以避免日志文件无限增长，同时使得日志易于查找和管理。

以下是一些常见的滚动策略：

1. 基于大小的滚动策略（Size-Based Rolling Policy）：当日志文件大小达到指定值时，创建一个新的日志文件。例如，在 Logback 中，可以使用 `ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy` 来实现这种策略。

2. 基于时间的滚动策略（Time-Based Rolling Policy）：根据时间间隔（如每天、每小时等）创建新的日志文件。例如，在 Logback 中，可以使用 `ch.qos.logback.core.rolling.TimeBasedRollingPolicy` 来实现这种策略。

3. 混合滚动策略：结合基于大小和基于时间的滚动策略，当满足其中任一条件时，创建新的日志文件。例如，在 Logback 中，可以将 `SizeBasedTriggeringPolicy` 和 `TimeBasedRollingPolicy` 一起使用。

此外，滚动策略还可以包含日志文件的清理策略，如最大日志文件数量、最长日志保留期限等。在达到这些限制时，最早的日志文件将被自动删除。

以 Logback 的 `TimeBasedRollingPolicy` 为例，以下是一个配置示例：

```xml
<appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>logs/app.log</file>
    <encoder>
        <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
    </encoder>
    <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
        <!-- 每天滚动日志文件 -->
        <fileNamePattern>logs/app-%d{yyyy-MM-dd}.log</fileNamePattern>
        <!-- 保留最近30天的日志 -->
        <maxHistory>30</maxHistory>
    </rollingPolicy>
</appender>
```

在这个示例中，滚动策略被设置为每天创建一个新的日志文件，同时保留最近 30 天的日志。当超过 30 天时，最早的日志文件将被自动删除。

滚动策略在日志管理中起着重要作用，有助于防止日志文件过大，提高日志文件的可读性和可维护性。要了解更多关于滚动策略的详细信息，请参阅相应日志框架的官方文档。



# 好用的工具类

## jackson

Jackson是一个Java语言的JSON库，用于在Java对象和JSON数据之间进行转换。它可以将Java对象序列化为JSON字符串，也可以将JSON字符串反序列化为Java对象。Jackson可以处理任意复杂度的Java对象，包括对象的继承关系、嵌套关系、集合和映射等。同时，Jackson还支持各种常见的JSON数据格式，包括JSON对象、JSON数组、JSON字符串、JSON数值、JSON布尔值和JSON null值等。

Jackson是一个功能强大、高效稳定的JSON库，在Java开发中被广泛使用。Jackson的主要优点包括：

1. 速度快：Jackson采用了高效的JSON处理算法，可以快速地将Java对象序列化为JSON字符串或者将JSON字符串反序列化为Java对象。
2. 易于使用：Jackson提供了简单易用的API，开发者可以快速地上手并进行相关操作。
3. 可扩展性强：Jackson提供了丰富的注解和接口，可以方便地扩展和定制自己的序列化和反序列化处理逻辑。
4. 配置灵活：Jackson支持各种配置选项，可以控制序列化和反序列化的行为，满足不同应用场景的需求。
5. 开源免费：Jackson是一款开源的JSON库，可以免费使用，并且有一个活跃的社区在维护和更新它的功能。

### 导入依赖

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

> 如果导入了springboot web模块的话,这个包已经帮我们导入好了

### 常用方法

Jackson提供了很多实用的方法，以下是一些常用的方法：

#### ObjectMapper.writeValueAsString(Object obj)

该方法将Java对象序列化为JSON字符串，并返回字符串表示。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
Person person = new Person("张三", 25);
String json = objectMapper.writeValueAsString(person);
System.out.println(json); // 输出：{"name":"张三","age":25}
```

#### ObjectMapper.writeValue(File file, Object obj)

该方法将Java对象序列化为JSON字符串，并将结果写入指定的文件。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
Person person = new Person("张三", 25);
File file = new File("person.json");
objectMapper.writeValue(file, person);
```

#### `ObjectMapper.readValue(String json, Class<T> valueType)`

该方法将JSON字符串反序列化为Java对象，并返回Java对象的实例。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
String json = "{\"name\":\"张三\",\"age\":25}";
Person person = objectMapper.readValue(json, Person.class);
System.out.println(person.getName()); // 输出：张三
```

#### `ObjectMapper.readValue(File file, Class<T> valueType)`

该方法将JSON文件反序列化为Java对象，并返回Java对象的实例。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
File file = new File("person.json");
Person person = objectMapper.readValue(file, Person.class);
```

#### `JsonNode.get(String fieldName)`

该方法获取JSON节点中指定字段名对应的节点。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
String json = "{\"name\":\"张三\",\"age\":25}";
JsonNode jsonNode = objectMapper.readTree(json);
String name = jsonNode.get("name").asText();
int age = jsonNode.get("age").asInt();
```

#### `JsonNode.iterator()`

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

#### `JsonNode.isArray()`

该方法判断JSON节点是否为数组类型。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
String json = "{\"name\":\"张三\",\"friends\":[{\"name\":\"李四\",\"age\":28},{\"name\":\"王五\",\"age\":30}]}";
JsonNode jsonNode = objectMapper.readTree(json);
if (jsonNode.get("friends").isArray()) {
    // ...
}
```

#### `JsonNode.isObject()`

该方法判断JSON节点是否为对象类型。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
String json = "{\"name\":\"张三\",\"friends\":[{\"name\":\"李四\",\"age\":28},{\"name\":\"王五\",\"age\":30}]}";
JsonNode jsonNode = objectMapper.readTree(json);
if (jsonNode.isObject()) {
    // ...
}
```

#### `ObjectNode.put(String fieldName, JsonNode value)`

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

#### `ArrayNode.add(JsonNode value)`

该方法向JSON数组节点中添加一个子节点。例如：

```java
ObjectMapper objectMapper = new ObjectMapper();
ArrayNode arrayNode = objectMapper.createArrayNode();
arrayNode.add(objectMapper.createObjectNode().put("name", "李四").put("age", 28));
arrayNode.add(objectMapper.createObjectNode().put("name", "王五").put("age", 30));
```

以上是Jackson库中一些常用的方法，可以满足大部分的需求。当然，Jackson还提供了很多其他的方法，开发者可以根据自己的需要进行查阅和使用。

### 常用注解

Jackson提供了许多注解，用于控制Java对象和JSON数据之间的转换。以下是一些常用的Jackson注解：

#### `@JsonAnyGetter`和`@JsonAnySetter`

**`@JsonAnyGetter`和`@JsonAnySetter`注解可以用于处理一些未知的属性**。`@JsonAnyGetter`注解标注在任意属性的获取方法上，`@JsonAnySetter`注解标注在任意属性的设置方法上。使用这两个注解可以让Jackson在序列化和反序列化时忽略一些不确定的属性。举个例子:

```java
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import java.util.HashMap;
import java.util.Map;

public class Person {
    private String name;
    private int age;
    private Map<String, Object> properties = new HashMap<>();

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @JsonAnyGetter
    public Map<String, Object> getProperties() {
        return properties;
    }

    @JsonAnySetter
    public void setProperty(String key, Object value) {  // 要注意这里的区别啊,不是直接设置整个对象
        properties.put(key, value);
    }
}

```

在这个 `Person` 类中，我们有 `name` 和 `age` 两个属性，以及一个名为 `properties` 的 `Map`。我们使用 `@JsonAnyGetter` 注解 `getProperties()` 方法，使得在序列化时，`properties` 中的**键值对会被平铺到最外层 JSON 对象**。我们使用 `@JsonAnySetter` 注解 `setProperty()` 方法，使得在反序列化时，**JSON 对象中未知的属性**可以被添加到 `properties` 中。

#### `@JsonProperty`

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

#### `@JsonIgnore`

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

#### `@JsonFormat`

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

#### `@JsonInclude`

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

### 补充说明

1. jackson 底层 通过反射拿到所有字段, 然后查看该字段的一些注解信息,然后查看该字段是否具有get,set方法,如果有,就调用,并根据规则序列化和反序列化数据,  如果没有, 就看是否有特定的注解,比如JsonProperty,如果有,也可以根据规则序列化和反序列化数据,如果没有,则查看它是public还是其他修饰符,如果是public就进行序列化与反序列化,如果没有的话就不对这个字段进行操作
2. Jackson在序列化的过程中, 如果没有一个可以序列化的字段,那就会抛出异常, 反序列化的过程中, 如果字符串对应的数据,没有被解析到对象中,就会抛出异常

当然,这个只是默认规则, 我们可以通过配置ObjectMapper 来指定这些规则

`ObjectMapper`提供了一系列的配置选项，允许您自定义序列化和反序列化的行为。以下是一些常用的配置规则及其用途：

1. `DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES`：控制反序列化时是否在遇到未知属性（不存在于目标Java对象中的属性）时抛出异常。默认为`true`。设置为`false`时，遇到未知属性将不会抛出异常，而是忽略它们。
2. `DeserializationFeature.FAIL_ON_NULL_FOR_PRIMITIVES`：控制反序列化时是否在将JSON属性值设置为null时抛出异常。默认为`false`。设置为`true`时，如果尝试将原始类型字段设置为null，则会抛出异常。
3. `DeserializationFeature.ACCEPT_SINGLE_VALUE_AS_ARRAY`：控制反序列化时是否允许将单个值作为数组处理。默认为`false`。设置为`true`时，允许将单个值作为数组处理，例如将`{"value": 1}`解析为`{"value": [1]}`。
4. `SerializationFeature.WRAP_ROOT_VALUE`：控制序列化时是否在根元素外添加包装元素。默认为`false`。设置为`true`时，将在根元素外添加包装元素，例如将`{"name": "John"}`序列化为`{"Person": {"name": "John"}}`。
5. `SerializationFeature.INDENT_OUTPUT`：控制序列化时是否对输出的JSON字符串进行缩进（格式化）。默认为`false`。设置为`true`时，输出的JSON字符串将被格式化，使其具有更好的可读性。
6. `SerializationFeature.WRITE_DATES_AS_TIMESTAMPS`：控制序列化时是否将日期类型（如`java.util.Date`）转换为时间戳。默认为`true`。设置为`false`时，日期将被格式化为字符串，例如`"2023-05-09T10:00:00.000+0000"`。
7. `SerializationFeature.FAIL_ON_EMPTY_BEANS`：控制序列化时是否在尝试序列化空对象（没有任何属性的对象）时抛出异常。默认为`true`。设置为`false`时，不会对空对象抛出异常，而是序列化为空JSON对象`{}`。

```
 // 序列化的时候,如果没有数据,也不报错
 objectMapper.configure(SerializationFeature.FAIL_ON_EMPTY_BEANS,false);
 
 // 如果反序列化的时候,遇到一个数据放不进去,也不报错
 objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES,false);
```



## Hutool

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



# 常用方法

## base64图片互转

base64转图片

```java
public void change(String data){
	    String[] parts = data.split(",");
        String base64Image = parts[1];
        String mimeType = parts[0].split(";")[0].split(":")[1];
        String fileExtension = mimeType.split("/")[1];

        byte[] decodedBytes = Base64.getDecoder().decode(base64Image);
        ByteArrayInputStream bais = new ByteArrayInputStream(decodedBytes);
        BufferedImage image;
        try {
            image = ImageIO.read(bais);
            if(image == null){
                System.out.println("image为空");
            }
        } catch (IOException e) {
            throw new RuntimeException("无法将字节数组转换为 BufferedImage", e);
        }

        if(Objects.equals(fileExtension, "jpeg")){  // 对于jpeg的话,这个库貌似不够转化,我们直接变成png
            fileExtension = "png";
        }
		
    	String path = "D:\\img\\"
        File ft = new FIle(path);
        if(!ft.exists())ft.mkdirs();
    
        String name = UUID.randomUUID() +"." +fileExtension;


        boolean png = ImageIO.write(image, fileExtension, new File(path + name));
}
```

反过来

```java
public void ImgToBase64() throws IOException {
        FileInputStream fileInputStream = new FileInputStream("D:\\img\\0a6dae19-7924-41c3-9edd-95aa659af5d1.png");

        String s = Base64.getEncoder().encodeToString(fileInputStream.readAllBytes());

        FileOutputStream fileOutputStream = new FileOutputStream("a.txt");
        fileOutputStream.write(("data:image/jpeg;base64," + s).getBytes(StandardCharsets.UTF_8));
        fileOutputStream.close();
    }
```



# 补充

## BeanFactory 和 FactoryBean

`BeanFactory` 和 `FactoryBean` 是 Spring 框架中两个重要的概念，它们在功能和用途上有一些区别。

1. `BeanFactory`：

`BeanFactory` 是 Spring 框架中最基本的容器，它负责管理和创建 Bean。`BeanFactory` 是一个接口，包含了 Bean 的创建、配置和管理的基本功能。在实际应用中，我们通常使用它的扩展接口 `ApplicationContext`，后者提供了更多的高级特性，如事件发布、国际化支持等。

主要功能：

- 负责创建和管理 Bean。
- 提供对 Bean 的依赖注入的支持。
- 实现了基本的 IoC（控制反转）容器功能。

2. `FactoryBean`：

`FactoryBean` 是一个接口，通常用于封装复杂对象的创建过程。当一个 Bean 的创建过程比较复杂，或者需要进行一些特殊的初始化操作时，可以考虑实现 `FactoryBean` 接口。这样，容器在获取 Bean 时，会调用 `FactoryBean` 的 `getObject()` 方法来创建 Bean 实例。

主要功能：

- 封装复杂对象的创建过程。
- 提供一种自定义 Bean 创建和初始化的机制。

总结：

- `BeanFactory` 是 Spring 容器的基础接口，负责创建和管理 Bean。实际应用中，通常使用 `ApplicationContext`。
- `FactoryBean` 是一个接口，用于封装复杂对象的创建过程。通过实现 `FactoryBean`，可以自定义 Bean 的创建和初始化逻辑。

以下是一个简单的 `FactoryBean` 示例：

```java
@Component
public class MyFactoryBean implements FactoryBean<MyObject> {

    @Override
    public MyObject getObject() throws Exception {
        // 创建和初始化 MyObject 实例
        MyObject myObject = new MyObject();
        myObject.initialize();
        return myObject;
    }

    @Override
    public Class<?> getObjectType() {
        return MyObject.class;
    }

    @Override
    public boolean isSingleton() {
        return true;
    }
}
```

在这个例子中，`MyFactoryBean` 实现了 `FactoryBean` 接口，并负责创建和初始化 `MyObject` 类的实例。当 Spring 容器需要获取 `MyObject` 类的实例时，会调用 `MyFactoryBean` 的 `getObject()` 方法。

## classpath

在 Spring Boot 中，`classpath` 是一个特殊的前缀，用于表示类路径。以下是关于 Spring Boot 中 `classpath` 路径的用法和注意点的总结：

1. 用法：
   - 在配置文件中，您可以使用 `classpath` 前缀来指定资源文件的路径。例如，`classpath:/templates/` 用于表示类路径下的 `/templates/` 目录。
   - 在 Java 代码中，您可以使用 `ResourceUtils.CLASSPATH_URL_PREFIX` 或直接使用字符串 "classpath:" 来加载类路径下的资源。

2. 注意点：
   - 当使用 `classpath` 前缀时，需要确保资源文件被正确打包到 JAR 或 WAR 文件中，以便在运行时可以被找到。
   - `classpath` 可以和通配符 `*` 一起使用，例如 `classpath*:/mapper/**/*.xml`，表示加载类路径下 `/mapper/` 目录及其子目录中所有的 `.xml` 文件。注意，`classpath*` 和 `classpath` 的行为略有不同：**classpath*会扫描所有类路径，而 classpath 只会扫描第一个匹配的类路径。**
   - 当使用 `classpath` 加载资源时，需要注意文件名的大小写，因为在某些操作系统（如 Linux）上，文件名是大小写敏感的。
   - 使用 `classpath` 加载资源时，还需要注意文件编码问题。如果资源文件包含特殊字符，需要确保文件的编码与读取时的编码一致。

了解这些用法和注意点有助于您在 Spring Boot 项目中更加高效地使用 `classpath` 路径。

## 资源路径问题

1. 静态资源路径：

   - 加载静态资源，如HTML、CSS、JavaScript等，Spring Boot默认从以下路径加载：
     - `/META-INF/resources/`
     - `/resources/`
     - `/static/`
     - `/public/`
     
   - 注意：这些路径是相对于类路径（classpath）的。它们通常位于项目的`src/main/resources`目录下。
   
   - 读取：使用相对路径访问静态资源。例如，`<img src="/images/logo.png">`。
   
   - 写入：通常不建议在静态资源目录下写入内容，因为它们可能会被覆盖。对于需要写入的文件，建议使用文件系统路径（见下文）。

2. 类路径（classpath）资源：

   - 类路径资源通常位于`src/main/resources`目录或`WEB-INF/classes`、`WEB-INF/lib`目录下。

   - 读取：使用`ClassLoader`的`getResourceAsStream()`方法或Spring的`ResourceLoader`获取资源。
     - 示例：`resourceLoader.getResource("classpath:config.properties")`
     
   - 写入：类路径资源通常是只读的。如果需要写入配置文件或其他资源文件，建议使用文件系统路径（见下文）。

3. Web应用上下文资源：

   - Web应用上下文资源位于Web应用的部署目录下。

   - 读取：使用`ServletContext`的`getResourceAsStream()`方法获取资源。
     - 示例：`servletContext.getResourceAsStream("/WEB-INF/config/config.xml")`

   - 写入：通常不建议在Web应用上下文目录下写入内容。对于需要写入的文件，建议使用文件系统路径（见下文）。

4. 文件系统资源：

   - 文件系统资源位于服务器的文件系统中。

   - 读取：使用Java的`File`类或`java.nio.file`包中的类来读取文件，或者使用Spring的`ResourceLoader`获取`file:`前缀的资源。
     - 示例：`resourceLoader.getResource("file:/path/to/file.txt")`

   - 写入：使用Java的`File`类或`java.nio.file`包中的类来写入文件。
     - 示例：
       ```java
       File file = new File("./path/to/file.txt");
       FileWriter fileWriter = new FileWriter(file);
       fileWriter.write("Hello, World!");
       fileWriter.close();
       ```

5. 外部配置文件路径：

   - 外部配置文件通常位于服务器文件系统中。

   - 读取：在`application.properties`或`application.yml`中指定配置文件路径，然后使用`@Value`注解或`@ConfigurationProperties`注解将配置文件的内容绑定到Java对象。
     - 示例：`@Value("${myapp.config.file-path}") private String configFilePath;`

   - 写入：使用Java的`File`类或`java.nio.file`包中的类来写入文件。
     
     * 示例：
       ```java
       File file = new File(configFilePath);
       FileWriter fileWriter = new FileWriter(file);
       fileWriter.write("key=value");
       fileWriter.close();
       ```

总结：

- 在Spring Boot项目中，资源路径可能是类路径资源、Web应用上下文资源、文件系统资源或外部配置文件路径。
- 这些路径的读写方式取决于它们的类型和位置。
- 类路径资源和Web应用上下文资源通常只用于读取。如果需要写入资源文件，推荐使用文件系统路径或外部配置文件路径。
- 当处理资源路径时，注意区分绝对路径和相对路径。绝对路径通常是相对于服务器文件系统的根目录，而相对路径是相对于类路径、Web应用根目录或其他基准路径。

## springboot打war包部署项目

### 新增配置类

继承SpringBootServletInitializer,然后重写configure方法

```
@SpringBootApplication
public class Demo5Application extends SpringBootServletInitializer {

    public static void main(String[] args) {
        SpringApplication.run(Demo5Application.class, args);
    }

    @Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder builder) {
        return builder.sources(Demo5Application.class);
    }
}

```

### 更改pom.xml

更改打包方式

```
<packaging>war</packaging>
```

更改依赖

```
		<dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-tomcat</artifactId>
            <scope>provided</scope>
         </dependency>
```

### 执行插件

```
mvn package
```

将war包放入webapps目录下

注意点:

* **配置文件里面的上下文路径是无效的,文件名字才是上下文路径**
* 一定要注意Tomcat和springboot的版本, 对应springboot3.0的话, 是改了servlet的包名的



## 新版本

现在已经有了springboot 3.0 和 spring6.0 了,但是啊, Java EE 已经变更为 Jakarta EE，包名以 javax开头的需要相应地变更为jakarta
