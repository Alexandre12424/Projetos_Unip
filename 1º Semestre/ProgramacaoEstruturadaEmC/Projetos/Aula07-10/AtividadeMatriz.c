#include <stdio.h>

int main()
{
  int matriz[4][4] = {
      {1, 2, 3, 4},
      {5, 6, 7, 8},
      {9, 10, 11, 12},
      {13, 14, 15, 16}};

  int i, j, soma = 0, somapar = 0;

  printf("Matriz original:\n");

  for (i = 0; i < 4; i++)
  {
    for (j = 0; j < 4; j++)
    {
      printf("%d ", matriz[i][j]);
      soma += matriz[i][j];
      if (matriz[i][j] % 2 == 0)
      {
        somapar += matriz[i][j];
      }
    }
    printf("\n");
  }

  printf("Soma dos elementos da matriz: %d\n", soma);
  printf("Soma dos elementos pares da matriz: %d\n", somapar);
}