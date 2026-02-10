#include <stdio.h>
int main()
{
  int contador = 0;
  int numero = 1;

  while (numero != 0)
  {
    if (contador < 3)
    {
      numero++;
    }
    else
    {
      numero = 0;
    }
    contador++;
  }
  printf("%d", contador);
  return 0;
}
