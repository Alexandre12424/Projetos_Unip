#include <stdio.h>
int main()
{
  int i, N = 5;
  int resultado = 0;
  for (i = 1; i < N; i++)
  {
    resultado = resultado + (i * 2);
  }
  printf("%d", resultado);
  return 0;
}
