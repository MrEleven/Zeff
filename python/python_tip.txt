在迭代的时候改变被迭代的对象所引发的问题

>>> class A(object):
...     name = ''
... 
>>> a = A()
>>> b = A()
>>> c = A()
>>> a.name = 'a'
>>> b.name = 'b'
>>> c.name = 'c'
>>> d.name = 'd'
>>> l = [a, b, c, d]
>>> for i in l:
...     if i == b:
...         l.remove(i)
...         continue
...     i.name = '123'
...
>>> for i in l:
...     print i.name
... 
123
c
123

解决方法

In [8]: a = [1,2,3,4,5,6]

In [9]: for i in a:
   ...:     if i == 3:
   ...:         a.remove(i)
   ...:     print i
   ...:     
1
2
3
5
6

In [10]: a = [1,2,3,4,5,6]

In [11]: for i in a[::-1]:
   ....:     if i == 3:
   ....:         a.remove(i)
   ....:     print i
   ....:     
6
5
4
3
2
1







>>> class A(object):
...     def __init__(self):
...         print '>>>A'
...         print '<<<A'
... 
>>> class B(A):
...     def __init__(self):
...         print '>>>B'
...         super(B, self).__init__()
...         print '<<<B'
... 
>>> class C(A):
...     def __init__(self):
...         print '>>>C'
...         super(C, self).__init__()
...         print '<<<C'
... 
>>> class D(B, C):
...     def __init__(self):
...         print '>>>D'
...         B.__init__(self)
...         print '<<<D'
... 
>>> d = D()
执行结果如下：
>>>D
>>>B
>>>C
>>>A
<<<A
<<<C
<<<B
<<<D
有意思的地方就在于，我在D的构造函数中调用B的构造函数，结果B的构造函数调用了A的构造函数，而B和A根本没有继承关系。

因为D的继承关系排序是这样的D B C A object。C在B的后面，所以super(B)会被误认为包括C。
Python中关于多继承有mro的东西，关于多继承的顺序有一个C3的算法。有兴趣可以去研究一下。

今天学会了一个有意思的函数apply,
apply就是以另外一种形式来调用函数
apply(func, args) 就相当于是func(*args)

今天还学会了用一个函数是一个字符串的方法，
str.capitalize()，这个方法可以使第一个字母变大写字母，使其他字母变成小写字母。
str.title() 的分割是以非字母字符来确定是否需要大写，
而string(module)中有一个方法string.capwords(str)类似雨str.title(),不过capwords是以空白字符为分割标准。

跟春哥打赌又输了。
class A(object):
    name = "eleven"

a = A()
a.__dict__是不包含name的。

sys.modules中包含所有当前进程中python虚拟机中的包

今天看Python源码的时候发现Guido超有意思，他总是把C语言的函数的返回值放在单独的一行。真是有意思的家伙，哈哈。

今天还是有收获的，发现很多python sdk都在导包的时候都喜欢用.来表示当前路径，今天的豆瓣sdk是这样，之前的淘宝sdk也是这样。一开始不知道什么意思，问了Django专家群中的大神们才明白这表示当前路径。不过至于什么时候适合用这种，什么时候适合写全路径。还不是很清楚。
