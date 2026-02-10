#include <stdio.h>

int main()
{
  int idade;
  float altura;
  char inicial;

  printf("Digite sua idade: ");
  scanf("%d", &idade);

  printf("Digite sua altura: ");
  scanf("%f", &altura);

  printf("Digite a inicial do seu nome: ");
  scanf(" %c", &inicial);

  printf("Sua idade: %d\n", idade);
  printf("Sua altura: %.2f\n", altura);
  printf("Sua inicial: %c\n", inicial);
  return 0;
}