#include "stdio.h"

#define ARRAYLEN 10

void sort(int* array, int len)
{
  int i = 0;
  int last = len;
  while(last--)
    {
      for(i=0; i< last; i++)
	{
	  if(array[i] > array[i+1])
	    {
	      int item = array[i];
	      array[i] = array[i+1];
	      array[i+1] = item;
	    }
	}
    }
}

int main()
{
  int i = 0;
  int array[ARRAYLEN] = {};
  for(i = 0; i< ARRAYLEN; i++)
    {
      scanf("%d", &array[i]);
    }
  sort(array, ARRAYLEN);
  for(i=0; i < ARRAYLEN; i++)
    {
      printf("%d ", array[i]);
    }
  printf("\n");
  return 0;
}
