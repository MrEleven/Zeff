int MAX_COLUMNS = 0;
int MAX_ROWS = 0;

int column = 0;
int row = 0;

// code1:
for (column = 0; column < MAX_COLUMNS; column++)
{
     for (row = 0; row < MAX_ROWS; row ++)
     {
	  table[ row ][ column ] = BlankTableElement();
     }
}

// code2:
for (row = 0; row < MAX_ROWS; row++)
{
     for (column = 0;column < MAX_COLUMNS; column ++)
     {
	  table[ row ][ column ] = BlankTableElement();
     }
}

// Code1的代码会比Code2的代码慢，因为code1会一直发生缺页中断。(MAX_ROWS * MAX_COLUMNS次) ，code2会发生MAX_ROWS次缺页中断。如果计算机内存大，则差异不明显，但是如果计算机内存小差异十分明显。
