今天看了手机中中的待办事项，发现还有好多问题没有解决。其中第一个就是关于协程。之前一直觉得很牛逼，居然可以交出执行权限。
今天终于理解了。原来是个纸老虎。其实交出执行权限就是一个goto语句，我也是很郁闷啊。

int function(void) {
     static int i, state = 0;
     switch (state) {
     case 0: goto LABEL0;
     case 1: goto LABEL1;
     }
LABEL0:
     for (i = 0; i < 10; i++) {
	  state = 1;
	  return i;
     LABEL1:;
     }
}

学一种新东西。当你觉得也就这么一回事的时候，你差不多已经理解它了。
如果你觉得这东西很神奇的时候，说明你还没有理解它。

加油，绝对清晰，是风格上唯一的美。对于x86的执行栈现在还没有绝对清晰，还需要复习《深入理解计算机系统》。明天回来看Linux内核的视频吧，上面也有讲x86的执行栈的。

给个链接吧：http://www.yeolar.com/note/2013/02/17/coroutines/