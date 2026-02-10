#include <stdio.h>
#include <locale.h>

int main()
{
  setlocale(LC_ALL, "Portuguese");

  int a = 5, b = 10;

  printf("a > 0 E b > 0: %d\n", (a > 0) && (b > 0));
  printf("a > 0 OU b < 0: %d\n", (a > 0) || (b < 0));
  printf("NÃO (a > b): %d\n", !(a > b));

  return 0;
}