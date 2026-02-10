#include <stdio.h>
#include <locale.h>

int main()
{
  setlocale(LC_ALL, "Portuguese");
  int num1, num2;

  printf("Digite o primeiro número inteiro: ");
  scanf("%f", &num1);

  printf("Digite o segundo número inteiro: ");
  scanf("%f", &num2);

  if (num1 > num2)
  {
    printf("O maior número é: %d", num1);
    printf("O menor número é: %d", num2);
  }
  else if (num2 > num1)
  {
    printf("O maior número é: %d", num2);
    printf("O menor número é: %d", num1);
  }
  else
  {
    printf("Os números são iguais.");
  }
}