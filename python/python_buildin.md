今天看了静爷去阿里面试，回来给我出了一道题目。如何优化开根号运算。其实之前我在网上看到过这道题目。回来在网上查了一下，发现有个叫牛顿迭代的东西，专门用来算这个的。（其实牛顿还是十分牛逼的。）大概的思路是这样的。
所谓开根号运算，就是求平方根。 
这个算法的核心思想是这样的a * a = b。x * y = b，如果x != y，那么x>a & y <a 或者x < a &  y > a。
所以在满足x*y = b的条件下，只要x,y 之间的差值越小，则越接近a。而(x + y)/2位于x, y之间。
所以(x + y) / 2 和 b / ((x + y) /2)肯定更接近a。依此规则递归下去，肯定可以找到一个十分接近a的值。

PS:python中原生Built-in命名控件中有个pow,就是用来表示阶乘的不过相对来说，我更喜欢用**来表示阶乘，这样写起来更方便。

python中属性用得不多，但是属性真的很好用，尤其是对于C#这种强类型的高级语言来说。说道这里我又想起来了，C#中一些十分细节的东西，其实C#的包装器除了get/set之外，还有另外一组包装器(add/remove)一般是用在事件代理方面。

class C(object):
    def __init__(self):
        self._x = None
       
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
        
    #用于删除属性， del c.x
    @x.deleter
    def x(self):
        del self._x
        
讲点我已经知道很久的，怕自己忘记，还是记一下比较好
xrange和range的主要区别是，一个是生成器，一个是普通序列

今天看python Built-in部分，还是发现不少漂亮的语法的。之前一直使用a.__dict__的方式获取a中的一些基本属性，但是今天看到vars()这个原生函数，a.__dict__就相当于vars(a)，这两者的结果是一样的。

关于zip，这个方法之前在公司的Python一行挑战中很流行(不过我始终坚持我的列表解析),zip的方法类似与矩阵乘法，
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> z = zip(x, y)
>>> z
[(1, 4), (2, 5), (3, 6)]
# 下面这个比较有意思
>>> a, b = zip(*z)
>>> a, b
((1, 2, 3), (4, 5, 6))


__import__这家伙之前在看tornado源码的时候就已经会用了，这里mark一下。
spam = __import__('spam', globals(), locals(), [], -1)
如果模块不在当前目录下，第四个参数(fromlist)专门用来写要导入的模块。注意：__import__()方法目前我只知道怎么导模块，不知道怎么像from ... import ...这样导入方法或变量。

对了，今天还看到了basestring()，这个东西之前在tornado源码中看到过，一直以为是tornado自带的，没想到是python自带的。basestring是unicode和str的基类，不能实例化。但是isinstance(obj, (str, unicode))就可以写撑isinstance(obj, basestring)了。

sorted（）这个方法也比较有意思
>>> class Student:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))

>>> student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]
>>> sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> from operator import itemgetter, attrgetter

>>> sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


PS：今天就先到这里吧，累得要命，顺便说一下，最近工作的事情超不爽。都没时间自己看书。Fuck.