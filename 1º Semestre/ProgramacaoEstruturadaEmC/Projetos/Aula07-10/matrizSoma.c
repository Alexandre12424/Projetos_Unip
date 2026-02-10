#include <stdio.h>

int main()
{
  int lin = 5, col = 2;
  int matriz[lin][col], i, j;

  for (i = 0; i < lin; i++)
  {
    for (j = 0; j < col; j++)
    {
      matriz[i][j] = i + j;
    }
  }

  printf("Matriz preenchida com i + j:\n");

  for (i = 0; i < lin; i++)
  {
    for (j = 0; j < col; j++)
    {
      printf("%d ", matriz[i][j]);
    }
    printf("\n");
  }

  return 0;
}