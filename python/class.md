今天看了python源码剖析的class部分。看完了，有很多体会，原来Python中函数和class都只不过是一个命名空间而已。metaclass是class的class，在python中所有的对象都是继承自object，这一点和C#是一样的。默认情况下，一个class的metaclass是type。之前在网上看到有人说django的ORM就是通过重写元类实现的。
还有这一章老是提到一个description这个鸟东西。现在还不是很清楚，只知道这个东西是slot的一个包装器，用来将slot包装成一个PyObject，这样才能被Python虚拟机调用。
今天还看到很早以前曾经想弄明白的一个修饰器staticmethod，在class中呗staticmethod修饰的函数就和全局普通函数差不多。而且它也不会通过PyMethod来转换。说道PyMethod这个鸟东西还是挺有意思的，PyMethodObject其实就是PyFunctionObject，只不过在调用bound函数的时候，在pfunc的时候保存了调用它的实例对象，这样就可以不用传self这个实例了，不过instance每次调用自己的实例方法的时候都会重新绑定，这样会比较耗性能，一个可行的方法是将返回的PyMethodObject保存下来。
class A(object):
    def f(self):
        pass
a = A()
for i in range(100):
    a.f()
#### 这样做的话f()就绑定了100次
func = a.f
for i in range(100):
    func()
#### 这样做的华f()就绑定了1次

记住一句牛逼的话:绝对清晰，是风格上唯一的美。
