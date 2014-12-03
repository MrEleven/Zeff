#include "stdio.h"

#define ARRAYLEN 10
void sort(int* array, int len)
{
  int i = 0;
  for(i=1;i<len;i++)
    {
      int base = array[i];
      int j = i;
      for(j=i-1;j>=0;j--)
	{
	  if(array[j]> base)
	    {
	      array[j+1] = array[j];
	    }
	  else
	    {
	      array[j + 1] = base;
	      break;
	    }
	}
      if(j == -1)
	{
	  array[0] = base;
	}
      int k = 0;
      for(k=0;k<len;k++)
	{
	  printf("%d ", array[k]);
	}
      printf("\n");
    }
}

int main(void)
{
  int array[ARRAYLEN] = {};
  int i = 0;
  for(i=0;i<ARRAYLEN;i++)
    {
      scanf("%d", &array[i]);
    }
  sort(array, ARRAYLEN);
  for(i=0;i<ARRAYLEN;i++)
    {
      printf("%d ", array[i]);
    }
  printf("\n");
  return 0;
}
