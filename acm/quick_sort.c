#include "stdio.h"

#define ARRAYLEN 10

void sort(int* array, int len)
{
	int xx = 0;
	if(len == 1 || len == 0)
	{
		return;
	}
/*	if(len == 2)
	{
		if(array[0] > array[1])
		{
			int item = array[0];
			array[0] = array[1];
			array[1] = item;
		}
		return;
	}
*/	int i = 0;
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
