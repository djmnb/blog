---
title: webMagic使用详解
date: 2023-2-15
---





webmagic  里面维持了一个请求队列,多个线程就是从这个队列里面请求

```java
 public static void main(String[] args) {
        Spider spider = Spider.create(new test1()).thread(5);  // 开启五个线程去请求队列里面拿请求,然后请求服务器
        for(int i=0;i<10;i++){
            spider.addUrl("http://localhost:8888/?a="+i);  // 请求这个地址会返回参数值
        }
        spider.run();
    }

输出结果如下:

get page: http://localhost:8888/?a=2
get page: http://localhost:8888/?a=1
get page: http://localhost:8888/?a=3
get page: http://localhost:8888/?a=0
get page: http://localhost:8888/?a=4
get page: http://localhost:8888/?a=8
get page: http://localhost:8888/?a=5
get page: http://localhost:8888/?a=9
get page: http://localhost:8888/?a=6
get page: http://localhost:8888/?a=7
```

