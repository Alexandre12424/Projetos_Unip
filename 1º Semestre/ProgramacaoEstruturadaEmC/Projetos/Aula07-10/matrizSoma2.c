#include <stdio.h>

int main()
{
  int m[3][3] = {
      {1, 2, 3},
      {4, 5, 6},
      {7, 8, 9}};

  int i, j, soma = 0;

  for (i = 0; i < 3; i++)
  {
    for (j = 0; j < 3; j++)
    {
      soma += m[i][j];
    }
  }

  printf("Soma dos elementos da matriz: %d\n", soma);

  return 0;
}