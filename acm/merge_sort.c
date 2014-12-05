#include "stdio.h"

#define ARRAYLEN 10


void mergearray(int* left, int left_len, int* right, int right_len, int* tmp)
{
	int i = 0;
	int j = 0;
	int k = 0;
	while(i<left_len && j < right_len)
	{
		if(left[i]<right[j])
		{
			tmp[k++] = left[i++];
		}
		else
		{
			tmp[k++] = right[j++];
		}
	}
	while(i<left_len)
	{
		tmp[k++] = left[i++];
	}
	while(j<right_len)
	{
		tmp[k++] = right[j++];
	}
	for(i=0;i<k;i++)
	{
		left[i] = tmp[i];
	}
}

void mergesort(int* array, int start, int end, int* tmp)
{
	int middle = (start + end) / 2;
	if(end == start)
	{
		return;
	}
	mergesort(array, start, middle, tmp);
	mergesort(array, middle+1, end, tmp);
	mergearray(&array[start], middle-start+1, &array[middle+1], end-middle, tmp);
}

void sort(int* array, int len, int* tmp)
{
	int first = 0;
	int last = len - 1;
	mergesort(array, first, last, tmp);
}

int main(void)
{
	int array[ARRAYLEN] = {};
	int tmp[ARRAYLEN] = {};
	int i = 0;
	for(i=0; i< ARRAYLEN; i++)
	{
		scanf("%d", &array[i]);
	}
	sort(array, ARRAYLEN, tmp);
	for(i=0; i< ARRAYLEN; i++)
	{
		printf("%d ", array[i]);
	}
	printf("\n");
	return 0;
}
