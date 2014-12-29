今天看到一个比较装逼得交换两个值得方法。
void inplace_swap(*int x, *int y)
{
	*y = *x ^ *y;
	*x = *x ^ *y;
	*y = *x ^ *y;
}
提醒一下，看不懂得朋友要注意运用a ^ a = 0;这个规律和位操作支持交换律和结合律。
这里其实存在一个潜在得bug。如果x和y指向同一个内存地址时会将这个地址得值置为0.

还有下面这个比较字符串长度的函数也时有bug的。
int strlonger(char *s, char *t) {
    return strlen(s) - strlen(t) >= 0;
}

其实strlen方法返回的类型时size_t类型，而size_t类型在stdio.h中被定义成unsignedd int类型。而两个无符号整形相减得到的还是无符号整形所以这个比较永远都返回1.


int main(void)
{
	usigned int len = 0xff0000ff;
	int x = (int)len;
	printf("%u\n", len);
	printf("%d\n", x);
	return 0;
}
这里输出的x是个负数。因为在强制类型转换的时候编译器只会变化解释的类型，而不会变化位模式。。所以变成了负数。
