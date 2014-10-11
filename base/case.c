#include "stdio.h"

int main(void)
{
    printf("挖掘机哪家强？\n");
    int a = 3;
    switch(a)
    {
final:
        case 0:
            printf("先到北大青鸟学1年，靠出计算机四级，再到蓝翔学1年，考出挖掘机四级，最后到新东方学1年，拿到厨师四级，这样就可以通过计算机控制挖掘机炒菜了，完美的职业规划!\n");
            break;
xindongfang:
        case 1:
            printf("新东方\n");
            break;
beidaqingniao:
        case 2:
            printf("北大青鸟\n");
            break;
lanxiang:
        case 3:
            printf("中国山东找蓝翔\n");
            goto final;
            break;
        default:
            printf("不是正规职业，少年还是不要学了\n");
            break;
    }
    return 0;
}

/*
 * 这个地方比较奇怪的是goto final之后，没有管case 0是否成立，直接就执行下去了。看来只能通过反汇编去看了。
 */
