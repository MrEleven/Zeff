a = 1
def g():
    print a

def f():
    print a
    a = 2
    print a

g()
f()

很多人会认为这段代码的执行结果会输出 1 1 2，其实这段代码执行到f()中第一个print的时候就会报错了:"local variable 'a' referenced before assignment"。根据LEGB的作用雨原则，f()的第一个a会用global空间中的值，但是结果却不是这样。

其实这个例子证明了python其实不是一门解释型语言，如果python和js一样是按行解释执行的，那么根据LEGB的原则会输出1。这里的问题就出在python需要编译。在编译生成pyc文件的时候，f()被看成是一个单独的命名空间，而这个空间中其实是存在a这个变量名的。所以在将语句翻译成字节码的时候，python把f()第一句翻译成了# LOAD_FAST # PRINT_ITEM # PRINT_NEWLINE，而g()中第一句翻译成了# LOAD_GLOBAL # PRINT_ITEM # PRINT_NEWLINE。具体python编译的时候如何确定字节码我现在还不清楚，不过可以肯定的是肯定是先确定命名空间中的变量名，然后再来翻译字节码。而当虚拟机执行LOAD_FAST的时候，发现当前命名空间中a的约束还没有建立，所以抛出了未引用的异常。

另外Python解释器的工作原理就和exe文件在x86CPU中执行的原理类似。PyFrameObject这个对象代表了Python解释器中的栈帧。

frameobject.h
typedef struct _frame {
	PyObject_VAR_HEAD
	struct _frame *f_back;
	PyCodeObject *f_code;
	PyObject *f_builtins;
	PyObject *f_globals;
	PyObject *f_locals;
	PyObject **f_valuestack;
	PyObject **f_stacktop;
	...
	int f_lasti;
	int f_lineno;
	PyObject *f_localsplus[1];
} PyFrameObject;
可以通过sys模块中的_getframe()方法获得当前python解释器正在运行的栈帧的PyFrameObject对象。
