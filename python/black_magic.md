今天学到两个比较有意思的黑魔法

__slots__ 这个包装器可以帮你限定这个类的实例能增加的字段。

<pre>
In [1]: class A(object):
   ...:     __slots__ = ("name", "sex", "age")
      ...:

In [2]: a = A()

In [3]: a.name = "eleven"

In [4]: a.name
Out[4]: 'eleven'

In [5]: a.hobby = "coding"
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-5-e6842dcc3e76> in <module>()
----> 1 a.hobby = "coding"
AttributeError: 'A' object has no attribute 'hobby'
</pre>



__all__ 这个包装器可以帮你限制导入的属性。。。

<pre>
# imptest/eleven.py
print 'eleven imported'

# imptest/yumi.py
print 'yumi imported'

# imptest/__init__.py
__all__ = ['yumi']

# python interpreter
In [1]: from imptest import *
yumi imported

</pre>

多看开源项目的代码，果然会有很大收获。

参考:https://docs.python.org/2/tutorial/modules.html
someting about black magic: http://www.pythontip.com/blog/post/4159/
