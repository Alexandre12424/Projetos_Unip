#include <stdio.h>
#include <locale.h>

int main()
{
  setlocale(LC_ALL, "Portuguese");
  int i = 5;
  printf("Valor de i: %d\n", i);
  printf("Pós-incremento: %d\n", i++);
  printf("Valor de i após pós-incremento: %d\n", i);
  printf("Pré-decremento: %d\n", --i);

  return 0;
}