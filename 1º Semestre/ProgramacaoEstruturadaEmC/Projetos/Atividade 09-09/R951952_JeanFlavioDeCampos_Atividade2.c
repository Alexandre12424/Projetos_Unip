#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main()
{
  setlocale(LC_ALL, "Portuguese");
  int i = 0, entrada, soma = 0;

  printf("Digite números inteiros (Digite 0 para parar): \n");
  scanf("%d", &entrada);

  while (entrada > 0)
  {
    soma += entrada;
    i++;
    scanf("%d", &entrada);
  }

  if (soma == 0)
  {
    printf("Nenhum valor digitado!");
  }
  else
  {
    printf("A soma dos números digitados é: %d\n", soma);
    int media = soma / i;
    printf("A média dos números é: %d", media);
  }
  return 0;
}