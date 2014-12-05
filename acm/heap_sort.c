#include "stdio.h"

#define ARRAYLEN 11


/*    0
 *  1     2
 *3  4  5   6
7 8 9
*/

int numb[] = {0, 1, 2, 10, 4, 3, 6, 7, 8, 9, 5};

void heap_adjust(int* array, int i, int size)
{
	int lchild = i * 2;
	int rchild = lchild + 1;
	int max = i;
	if(i <= size/2)	// 判断是否是叶子节点
	{
		if(array[lchild] > array[max])
		{
			max = lchild;
		}
		if(rchild <= size && array[rchild]>array[max])
		{
			max = rchild;
		}
		if(max != i)
		{
			int item = array[max];
			array[max] = array[i];
			array[i] = item;
			heap_adjust(array, max, size);
		}
	}
}

void build_heap(int* array, int len)
{
	int i = 0;
	for(i=len/2;i>0;i--)
	{
		heap_adjust(array, i, len);
	}
}

void heap_sort(int* array, int len)
{
	build_heap(array, len);
	int i = 0;
	for(i=len;i>0;i--)
	{
		int item = array[1];
		array[1] = array[i];
		array[i] = item;
		heap_adjust(array, 1, i-1);
	}
}

int main(void)
{
 	int array[ARRAYLEN] = {};
	int i = 0;
	for(i=1; i< ARRAYLEN; i++)
	{
		scanf("%d", &array[i]);
	}
	heap_sort(array, ARRAYLEN-1);
	for(i=1; i< ARRAYLEN; i++)
	{
		printf("%d ", array[i]);
	}
	printf("\n");
	return 0;
}
