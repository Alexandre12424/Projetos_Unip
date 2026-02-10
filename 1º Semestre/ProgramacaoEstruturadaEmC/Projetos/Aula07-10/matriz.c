#include <stdio.h>

int main()
{
  int matriz[3][3];
  matriz[0][0] = 10;
  matriz[0][1] = 20;
  matriz[0][2] = 30;
  matriz[1][0] = 40;
  matriz[1][1] = 50;
  matriz[1][2] = 60;
  matriz[2][0] = 70;
  matriz[2][1] = 80;
  matriz[2][2] = 90;
  /*
    int matriz[3][3] = {
        {10, 20, 30},
        {40, 50, 60},
        {70, 80, 90}};
  */
  for (int i = 0; i <= 2; i++)
  {
    for (int j = 0; j < 3; j++)
    {
      printf("%d ", matriz[i][j]);
    }
    printf("\n");
  }
  return 0;
}