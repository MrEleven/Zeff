跟端端聊天以后发现自己还是太水，于是又重新开始看《深入理解计算机系统》。

首先说一下，为什么32位字长的机器最多只能使用4G的内存。
首先字长是什么？在我的理解中字长就是CPU总线的宽度（可能只是地址总线的宽度）。
CPU总线的宽度为32位，则表示最多能表示2^32个地址。
内存的编码单位是以字节来编码的，每个地址表示一个字节。
所以一共可以表示2^32个字节也就是4GB。

关于查看数据在计算机中的二进制表示(其实是16进制)，当然也可以用这个方法来确定计算机的大小端
#include <stdio.h>

typedef unsigned char *byte_pointer;

void show_bytes(byte_pointer start, int len){
     int i;
     for( i = 0; i < len; i++){
	  printf(" %.2x", start[i]);
     }
     printf("\n");
}

void show_int(int x){
     show_bytes((byte_pointer) &x, sizeof(int));
}

int main(int argc, char *argv[]){
     show_int(0x1234);
     return 0;
}
刚刚试了一下，发现自己的电脑是小端机器。哈哈。
等我的《C语言程序设计》到了，马上就能开始C语言的修行之路了。熟悉了以后就可以开始通往Linux内核的道路了。
