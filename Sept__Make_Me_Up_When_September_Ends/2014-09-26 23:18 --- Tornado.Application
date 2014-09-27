关于Tornado的Application对象
default_host --- 默认主机，如果找不到对应host的handler，则将页面跳转到http://{{default_host}}/页面（只是个猜测，我没有测试过）。

transforms --- 这个不知道是干嘛的。

ui_modules --- 指定当前application对象的ui模块，可以传模块，list和UIModule

ui_method --- 制定当前application的ui_method对象，同样可以传module, list和func。（ui_method就是那些在template中定义的方法）

static_path --- 静态文件地址

static_url_prefix --- 静态文件请求的url前缀，默认是/static/

static_handler_class --- 静态文件对应的处理类型，默认是tornado自带的StaticFileHandler，可以自己写。

static_handler_args --- 静态文件处理类型的参数

 

listen(self, port, address="", **kwargs) 方法创建一个HTTPServer实例，然后调用这个实例的listen()方法。注释中特别说明，如果是多线程的用法不能用该函数，需要显示调用HTTPServer或TCPServer自己的方法。

add_handlers(self, host_pattern, host_handlers)方法的作用是往self.handler中添加handler。这里需要注意如果handler匹配的url中有通配符，那么这个handler的优先级就会下降(排到了后面)，如果添加相同的正则表达式会tornado会报异常。

add_transform（self, transform_class）这个函数是往self.transforms增加transform_class，但是transforms到底用来干什么我还不知道。

_load_ui_methods(self, methods)往self.ui_methods中添加方法

_load_ui_modules(self, modules)与_load_ui_method的功能是一样的。

reverse_url(self, name, *args)这个方法不知道是用来干嘛的。

log_request(self, handler)这个方法是吧请求写进日志，http状态小于400的都是属于正常状态，大于等于400小于500的都属于警告状态，除了上面的状态之外的都是错误状态。

_get_host_handlers(self, request)这个方法会根据request的host寻找属于这个的handlers，

__call__(self, request)方法使application实例对象变成可调用，它会调用_get_host_handlers()，将获取到的handlers再根据path来确定具体要使用的handler。它做了一些处理，比如如果没有找到对应host的handlers，那么直接跳转到默认host下面。如果没有找到匹配的Handler那么跳转到默认页面或者抛出404异常。另外它还会根据配置决定是否cache编译好的template文件，是否cache静态文件。

另外我还从代码中发现，如果是debug模式，默认会开启autoreload和serve_traceback功能，关闭compiled_template_cache和static_hash_cache功能，你可以通过在Application的__init__()函数中开启他们。

 

python 中 setdefault()方法还是很有用的，如果字典中没有这个值，那么就添加并赋值，如果有就忽略本次操作。

>>> a = {"name": "eleven"}
>>> print a
{'name': 'eleven'}
>>> a.setdefault("name", "yumi")
'eleven'
>>> a.setdefault("age", 23)
23
>>> print a
{'age': 23, 'name': 'eleven'}
dict中get()方法在不传第二个参数的情况下如果没有指定的键会返回None，不会报错，我之前还一直指定第二个参数为None。

>>> b = {}
>>> print repr(b.get("name"))
None
python中or操作就相当于是C中的三目运算符?:

>>> 1 or []
1
>>> 0 or []
[]
>>> 1 if 1 else []
1
>>> 0 if 0 else []
[]