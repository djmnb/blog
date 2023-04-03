## http协议

## 计算机网络:

​	

	协议三要素:
		语法:
		语义:
		同步:

## vue 

## javase



## javaweb 

	1.url-pattern几种形式
	
	2.同一个Tomcat下的不同应用之间seesion是共享的嘛?
	
	3.

## mysql
​	数据源的作用:
​		我们自己在使用jdbc连接数据库时,总是频繁的创建销毁连接,这样效率的非常低的,数据源帮我们管理这些连接,
​		避免了频繁的创建与销毁连接(不过有的数据源也没有提供连接池的功能)



## maven

## git

## spring

	bean的生命周期:
		实例化,属性设置,初始化,销毁
	bean的作用域:
		单例,原型,请求域,session,application
	
	什么是IOC
		控制反转,实现对象之间的解耦
		通过IOC容器,利用相互依赖关系注入的方式,实现对对象之间的解耦


​	

	什么是aop
		aop是面向切面编程,实现程序功能统一维护的一种技术(动态代理(不修改源代码的情况下增强功能,进行解耦合,提高程序的可重用性))
		作用:就是动态代理的作用
		优势:减少代码重复,提高开发效率,便于维护
	
		连接点:就是类中被增强的方法
		切入点:包含哪些类的哪些方法要被增减
		通知:增强方法执行前还是执行后要执行的方法
		切面:切入点+通知 
	
		spring中使用aop:
			导入aspectjweave坐标
			xml格式:
				声明aop自动代理
				<aop:aspectj-autoproxy>
			纯注解模式
			       后续学了再来总结
	        哪些地方使用了aop:
			事务控制,日志,异常处理


​	
​	

	aop的通知类型:
		@Before
		@AfterReturning
		@Around
		@AfterThrowing
		@After
	
		上面几个注解修饰的方法,必须是public的,参数都可以放一个JoinPoint类型的参数,
		他可以用来获取连接的信息,比如名字啊,参数类型啊
	
		其他类型的参数就可以按照这个名字的意思来看了
	切入点表达式可以有哪些:


	利用自定义注解+aop 实现日志打印的功能


	spring事务管理:
		1.编程式:自己写开启事务,提交事务,回滚事务(不太好用)
		2.声明式:不入侵业务代码



		PlatformTranscationManager:事务管理器(定义了事务的一些行为)(不同的技术事务管理器可能不一样)
		TranscationDefinition:事务的定义信息(事务的隔离级别,事务的传播行为,是否只读,超时时间)
		Transcstatus:事务执行的状态(是否提交,是否回滚)


	spring的一些后置处理器及其作用:
		
		1.BeanFactoryPostProcessor:
			 void postProcessBeanFactory(ConfigurableListableBeanFactory var1)
			此时所有bean的定义信息已经被全部加载,但是还未实例化
			用于bean实例化前执行的方法
		2.BeanDefinitionRegistryPostProcessor:
			postProcessBeanDefinitionRegistry(BeanDefinitionRegistry var1)
			此时所有bean的定义信息将要被加载(里面有一部分了,也还有一部分没有加载进来,
			因为这个接口里面的方法可以注册bean的定义信息),也还没实例化,看方法里面的参数就知道,我们还能自己注册bean
		3.BeanPostProcessor:
			   里面定义了两个方法,分别用于bean的初始化前后执行
		
		4.InstantiationAwareBeanPostProcessor extends BeanPostProcessor:(注意和BeanPostProcessor的区别)
	
			 postProcessBeforeInstantiation(Class<?> beanClass, String beanName)
			里面定义了两个方法,分别用于bean的实例化前后执行,可以用于代理bean,
			因为容器是根据这里面的返回值确定容器里面放的bean是什么,看参数便知道,此时的bean尚未被创建
			我们可以自己创建然后对其进行代理,aop就是这么做的
		
		上面四个接口的执行顺序:
			2->1->4->3


​		
​	
​	spring 源码总结(以注解驱动为列子):
​		创建AnnotationConfigApplicationContext容器
​			this();
​				实例化IOC容器
​				往里面添加一些后置处理器的bean定义信息
​			this.register(componentClasses);
​				注册当前配置类
​			this.refresh()
​				
​				invokeBeanFactoryPostProcessors
​					invokeBeanDefinitionRegistryPostProcessors
​						先执行系统放进去的ConfigurationClassPostProcessor接口里面的方法,它会把所有的bean的定义信息加载到容器中
​						(此步骤主要是找到所有扫描到的bean,import,component这些注解的东西,并将这些bean的定义信息加载进来),
​						然后再根据优先级执行已经加载的bean里面的实现了BeanDefinitionRegistryPostProcessor的里面的方法,
​						并将这些bean给加载到容器中
​					
					invokeBeanFactoryPostProcessors
						执行所有已经注册bean的postProcessBeanFactory方法
				至此所有bean的定义信息已经被加载
	
				registerBeanPostProcessors();注册所有的BeanPostProcessor对应的bean
					从bean工厂里面拿到所有的BeanPostProcessor类型的bean定义信息,
					然后按照优先级的顺序依次将这些bean注册到容器中


				initMessageSource()初始化国际化信息
	
				initApplicationEventMulticaster();初始化事件派发器,其实就是看哪个事件监听器能够处理当前的事件
	
				registerListeners();注册所有事件监听器
	
				finishBeanFactoryInitialization();注册完毕所有的单实例bean
					如果当前bean是工厂bean,则注册工厂bean生成的那个对象,
					然后将生成其他没有实例化和初始化的bean



## mybatis

开发流程(简单maven工程中):
	1.导入坐标mybatis的jar包,数据库的驱动,数据源 如果是spring中还要导入spring-mybatis的jar包
	2.编写实体类以及操作数据库接口
	3.编写数据库接口对应的sql语句(mapper代理)
	4.编写mybatis配置文件(设置别名啊,设置属性,配置环境(数据源,事务管理器),mapper映射文件的位置)

可以使用typeAliases 对类型起别名,在sql子标签resulttype属性中就可以使用,但是我感觉没有啥用

#{} 与 ${} 的区别在于 前者会设置参数防止SQL注入,后者是直接拼接

如果数据库的表名与实体类的属性名不同可以使用下面两种方法:
	1.给数据库中取出的字段取别名
	2.使用resultmap给出一组对应关系(主键字段需要用<id>标签取别名)

xml中默认不允许使用<字符,如果需要使用,需要转义或者使用cd命名空间

传递参数的三种方式:
	多参数
		1.
			直接通过函数参数 当有多个参数的时候需要使用(@param("")注解,
			如果还是使用原来的那个参数名字会报错(因为有多个参数的时候,mybatis会把参数封装成一个map,然后键名就是arg0,arg1这些,建议全部使用@param注解)
	单参数:
		2.
			对象形式
		3.
			map形式

​	在配置文件中只需要使用 #{参数名|属性名|key值} 就可以拿到参数值


​	
​	
​	动态sql
​		当用户输入的参数个数不确定时,我们也可以只写一个sql语句让mybatis帮忙生成对应的sql语句
​		1. 动态查询
​			
​			<where> <if test=""> <where> 形式 test里面需要像sql


​	
​	当查询时出现一个实体类里面还出现了另外一些实体类时(一对一,一对多)
​		1.自定义resultmap 将对应的列封装到属性中,如果是属性是对象,resultmap中的属性名就写对象变量名字.属性名
​		(上面这种方法的缺点是需要重复太多的对象的变量名字)
​		
​		2.
​			对象:
​				<association property="" javatype=""(如果没有取别名,这里得写成包名路径+类名)> 
​				这样就不用写很多次对象变量名字(里面就跟平常写resultmap一样了)
​			集合:
​				<collection>


## springMVC


​	这个部分其实就是简化以前的javaweb 开发,对以前的代码进行了解耦合,以及提供了很强大的功能
​	
​	以前传统的javaweb太过于繁琐,需要自己继承servlet并且重写doGet,doPost方法,然后再在web.xml里面声明哪些servlet处理哪些请求
​	其实这些都是可以简化的,springMVC就帮我们做到了这些,它接收指定路径下的所有请求,将这些请求进行解析,
​	通过handlermapping对应的handler(其实就是找到哪个方法处理哪个请求),然后找到能够处理这个handler的适配器
​	(适配器就能够通过参数解析器(argumentsResolver)解析请求参数或者请求体,提供handler需要的参数,并执行它),
​	以及视图解析器,然后将数据返回给前端在这个过程中
​	

我们希望做到的就是,前端传来的数据,我们不去自己进行接收和类型转化,只声明一下函数参数的类型就行,springMVC通过反射拿到函数参数类型
找到适合的类型转化器,将这些前端传来的数据变成对应的类型再传进函数供我们使用,再将返回值进行处理

使用文件上传功能时,需要导入依赖,然后配置文件视图解析器,前端必须以post方式请求,以及使用multipart/form-data形式传递参数

请求所用注解
	@RequestParam 
		如果是get请求,那么使用此注解,只会解析路径上携带的参数,如果是post请求那么将路径上的参数和请求体里面的参数
		(如果路径上的参数名字与请求体里面参数名字相同,则会合并)
	@PathVariable 接收restful风格的路径参数

​	@RequestBody 
​		将请求体里面的所有数据全部拿来放到对应的参数里面,如果需要将里面的数据转换成java对象
​		(这种就只适合application/json格式的数据),需要开启webmvc注解驱动,并且导入json的包
​	@RequetPart
​		接收multipart/form-data 类型数据

响应注解
	@ResponseBody
		将返回值直接当成返回的内容给用户,如果想直接将返回值变成json格式,只需要开启webmvc注解驱动,然后加入json包

如果参数前面没有加任何注解,springMVC是将这个对象创建出来,然后用这个对象的set方法尝试将参数注入进去,
所以如果这个参数类型是接口那不行,如果属性没有set方法也不行

静态资源问题:由于springMVC代替了默认的servlet处理器,请求资源的时候也被springMVC处理了,但是,它里面没有这些请求,
所以得做一个资源映射,告诉springmvc这些资源路径对应的资源在哪

filter 与 拦截器
	filter 是 servlet的一部分任何Javaweb的工程都能够使用(只能设置过滤路径,如果要在这些过滤路径中排出一些不要过滤的,需要在代码中实现)
	拦截器属于springmvc的,只有在springmvc中才能使用(能设置拦截路径,也能设置不拦截路径)
	filter适合对所有请求做相同的事情,比如设置编码啊,往里面请求中添加东西啊
	拦截器就适合拦截,对哪些请求放行,哪些请求不放行


​	
​	
​	异常处理器:
​		将所有的异常进行统一的处理
​	
​		@RestControllerAdvice声明这个类时异常处理类
​		 @ExceptionHandler(Exception.class) 说明这个方法处理哪个异常
​	

​	这个就厉害了(它能够controller层拦截所有异常(404除外,因为它还没有进入controller层),请求参数不匹配啊.....)


​	
​	使用WebMvcConfigurationSupport+注解能够全面替代web.xml,原先在web.xml要配置的东西,都可以在这个配置类中写


​	

## springboot
	

如果一个组件只有一个有参构造器,那么他的所有构造器参数都会从容器中去取

@Import注解一般是用来导入一个配置类,这个类必须具备无参构造器否则会报错
@ImportResouce 是导入spring的xml格式的配置文件


​	springboot启动的时候会加载每个jar包下META-INF/spring.factories里面写好的自动配置类,一般是xxxxxAutoConfiguration
​	这些自动配置类会往容器里面注入很多的bean
​	
​	自己定制化的两种方式:
​		1.自己注册bean替换底层组件
​	

​		2.修改配置文件即可(一般能变的属性,springboot都是通过配置文件与属性配置类进行绑定,修改配置文件里面的值就能修改属性值)


​	
​	springboot默认不支持jsp



springMVC 执行流程
	由于dispatcherservlet接管了/请求,所以在springmvc中所有的请求都由dispatcherservlet来处理,请求处理映射器会把所有controller层的
	标注了requestmapping注解的方法全部记录起来,大体格式就是哪个请求对应哪个方法.
	当有请求来时,从请求处理映射器里面找到对应的handler(处理这个请求的方法),由于不同方式注册的请求对应的handler处理的方式不一样,
	需要再找到处理器适配器(springmvc里面有四个
		1.RequestMappingHandlerAdapter(根据requestmapping注解来找)
		2.HttpRequestHandlerAdapter
		3.HandlerFunctionAdapter
		4.SimpleControllerHandlerAdapter(根据url配置来找对应的controller,这个controller必须实现controller接口)
	)
	找到对应的适配后,就会执行处理此handler,首先会根据handler对应方法参数信息,找到对应的参数解析器,
	参数解析利用convert将请求参数或者请求体中的数据解析成形参对应的类型,然后就会通过反射执行方法,得到返回值,
	然后再根据返回值及handler的信息找到合适的返回值handler处理器然后进行内容协商,通过消息转化器将返回值解析成适合客户端的类型,
	最后将数据放入modelandview中,最后渲染页面或者直接返回数据给客户端

在dispatcherservlet中,任何handler执行完毕返回的 都是modelandview对象,里面包含数据,以及视图地址



springboot中好用的功能:
	shiro,jwt,async,socketio,,schedule,mybatis,mybatis-plus,