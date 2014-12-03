#include "stdio.h"

#define ARRAYLEN 10

void sort(int* array, int len)
{
	if(len == 1 || len == 0)
	{
		return;
	}
	int i = 0;
	int j = len-1;
	int base = array[0];
	int space = 0;
	while(i != j)
	{
		while(j > i && array[j] > base)
		{
			j--;
		}
		if(i == j)
		{
			break;
		}
		else
		{
			array[space] = array[j];
			space = j;
		}
		while(i < j && array[i] < base)
		{
			i++;
		}
		if(i<j)
		{
			array[space] = array[i];
			space = i;
		}
	}
	array[i] = base;
	sort(array, i);
	sort(&array[j+1], len-j-1);
}

int main(void)
{
	int array[ARRAYLEN] = {};
	int i = 0;
	for(i=0; i<ARRAYLEN; i++)
	{
		scanf("%d", &array[i]);
	}
	sort(array, ARRAYLEN);
	for(i=0;i<ARRAYLEN; i++)
	{
		printf("%d ", array[i]);
	}
	printf("\n");
	return 0;
}

快速排序还是很给力的。我觉得最牛逼的还是这个算法的发明者能够通过一个数组的空间进行排序，如果是我我肯定会开另外一个数组进行排序。
分治思想还是很牛逼的（不过采用了递归之后性能到底会不会比循环快这个我还没有测试过。）
排序算法介绍地址： http://developer.51cto.com/art/201403/430986.htm
