前段时间看了《C与指针》，今天又看了《C专家编程》，C专家编程阅读者的高度真的很高。我在想要不要学，估计以后我C语言的代码写的也不会很多。好在我把基本的《Python源码剖析》已经看完了。网络，语言，操作系统。几乎现在左右的东西都是基于C语言的。不过因为我在米帮上班，工作用的代码都是用Python写的，所以学好了Python能提高工作效率，这样我就有更多的时间来看自己的书了。

需要学的东西还有很多，最近越来越觉得算法比较重要，一些基本的数据结构比较重要，只是我之前忽略了这些东西。其实最近一段时间看了C语言的书之后越来越觉得C比Python牛逼。但是毕竟Python的代码比较优雅，而且现在的硬件已经不在乎那么一点点效率开销了。

还是那句老话，绝对清晰，是风格上唯一的美。对于Linux，现在也只是停留在shell阶段，内核什么的基本没接触，这样就没有办法接触内核中线程进程这些抽象的结构了。而且硬件方面也是十分缺乏。

今天在youtube上看了一个台湾的家伙讲的关于GCC编译器的东西，他的工作是帮助C编译器做优化工作。其中有个问题还是蛮有意思的。
int add(int *a, int *b)
{
    *a = 3;
    *b = 5;
    return (*a + *b);
}
为什么不能被优化成
int add(int *a, int *b)
{
    *a = 3;
    *b = 5;
    return (3 + *b);
}

原因很简单，因为用户比较奇葩，他可能给a, b传同一个值。好吧，逻辑真严密。呵呵。

今天继续看数据结构和算法。在淘宝上买了两本书，一本是讲计算机硬件和软件的知识的，感觉自己要补充一下自己未知的东西，这样才会更牛逼。另一本是《编程之美》，讲面试的。

还是早点睡觉吧，早睡早期身体好，绝对清晰是风格上唯一的美。

原来很多计算机中得小数是不是跟近似值不但跟精度有关系，而且跟数值也有关系。1/5=0.2，但是计算机没有办法准确表示0.2，因为小数部分得模是1/2，所以如果是8位表示，都适用51/256来表示得。

还有一个有意思得东西就是，如果f=Tmin，那么-f=Tmin。(再固定字长得计算机中，最小值的补数等于它本身。)
