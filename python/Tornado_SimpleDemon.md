前几天挺春哥讲sputnik的一些东西，感觉很帅。春哥就是牛逼，对tornado十分熟悉，感觉就像是他写的一样。
由于《Python源码剖析》还在快递叔叔那边，所以还是想看看tornado的东西吧，毕竟看这样的项目的代码一定会有很多收获的。

import tornado.httpserver   # 一个httpserver类
import tornado.ioloop       # IO循环在里面
import tornado.web          # tornado组件都在这里
import tornado.options      # 一些配置信息

from tornado.options import define, options

define("port", default=8000, help="run the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument("greeting", "Hello")
        self.write(greeting + "tornado")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        ("/index", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

tornado.httpserver 是一个服务器类。
tornado.ioloop 	   是一个io循环，tornado的核心就在这里
tornado.web	   这个是tornado web框架的核心组件
tornado.options	   tornado的一些配置信息

define() 这个函数可以定义一些变量，并且可以赋一些默认值，但是默认值之后会被命令行参数覆盖。
还有偷偷发现一点，貌似这个define()定义的变量是全局的，帅。
tornado/options.py文件中有一个变量options，这个变量是OptionParser类的一个实例。这个变量是包含了所有的配置信息，当然也可以通过define方法定义自己的全局变量。
define()这个方法其实也只是包装了options的一个实例方法。不知是什么原因， tornado中每个option的属性都是一个_Option实例，感觉直接写原生的python类型也可以。这样做的话，我们必须通过define创建我们自己的属性，而不能通过普通的赋值方式创建属性，但是可以用赋值的方式修改。因为OptionParser重写了__setattr__()方法，另外还有一个问题，就是那个Mockable类，这是在OpitionParser重新包装了一下。但是具体的原因跟Python类的实现机制有关，由于源码分析还有到，所以我决定先放一下，已经记到Plan.txt里面了。这里的define()定义了一个全局变量port。
tornado.web.RequestHandler之前我已经分析过了，就是一个处理http请求的类型，这里我就跳过了。
tornado.options.parse_cimmand_line()这个方法只要是从命令行分析参数，然后给之前定义的option赋值，如果没有赋值就使用默认值。
tornado.web.Application这个类是一个应用的抽象，之前我也已经分析过了，这里就跳过了。

tornado.httpserver.HTTPServer这个东西比较犀利，是一个http服务器的抽象。它是TCPServer的一个子类(因为HTTP是基于TCP实现的)。这两个家伙的实现相对来说也是比较复杂的，而且要有很好的http协议的基础。所以暂时也先放一放。
ioloop这是一个IO循环，tornado比django高效的原因就在这里，因为tornado是基于IO复用的IO模型实现的，所以比多进程的IO模式要高效得多。因此，tornado也只能运行在有epoll/select/poll这样的UNIX系统之上，而不能在windows上运行。异步IO这个东西比较复杂。以后放单独一个文件讲解。





在tornado.options中发现了一个我之前思考过的问题。这个问题就是datetime.datetime.strptime()这个方法如何比较智能地分析时间。
tornado中采取的方法是先写好一大堆format，然后用try/except的方法每个去匹配。虽然这样的做法不太好，但是我也想不出其他更优雅的方式。
之前是我们自己的项目，而且会产生的时间格式也只有固定几种，所以那个时候我是通过判断字符串长度来确定是哪种格式的日期格式。这里用try/except也不会有问题，因为所有的option都是唯一的，修改的几率很小很小。不用考虑性能问题。

