#include "stdio.h"

#define ARRAYLEN 10

void sort(int* array, int len)
{
	int last = len -1;
	for(last=len-1; last > 0; last--)
	{
		int max = array[0];
		int position = 0;
		int i = 0;
		for(i=1;i<=last; i++)
		{
			if(array[i] > max)
			{
				max = array[i];
				position = i;
			}
		}
		int sum = max + array[last];
		array[position] = sum - max;
		array[last] = sum - array[last];
	}
}

int main(void)
{
	int array[ARRAYLEN] = {};
	int i = 0;
	for(i=0; i< ARRAYLEN; i++)
	{
		scanf("%d", &array[i]);
	}
	sort(array, ARRAYLEN);
	for(i=0; i< ARRAYLEN; i++)
	{
		printf("%d ", array[i]);
	}
	printf("\n");
	return 0;
}
