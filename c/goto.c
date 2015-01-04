#include "stdio.h"
#include "string.h"

// 为了弄明白Python字节码中控制结构，必须先弄明白goto的语法，
// 坑跌的指令预测。不过发现其实goto是个好东西，我很喜欢这个关键字。
// 既然存在这个关键字，就一定有它存在的道理，好好利用就能写出很漂亮的语句。
int main(void)
{
    int i = 0;
    if(i == 1)
    {
        goto v1;
    }
    else if(i == 2)
    {
        goto v2;
    }
    else if(i == 3)
    {
        goto v3;
    }
    else
    {
        goto other;
    }
v1:
    printf("1\n");
v2:
    printf("2\n");
v3:
    printf("3\n");
other:
    printf("other\n");
    return 0;
}
