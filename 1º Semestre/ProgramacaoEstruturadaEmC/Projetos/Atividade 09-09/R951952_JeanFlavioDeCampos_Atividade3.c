// Enunciado
// Desenvolvam um programa em C que solicite ao usuário um número inteiro positivo para representar o número de linhas.
// Utilizando dois laços for aninhados, o programa deve imprimir um triângulo de asteriscos com o número de linhas informado, seguindo o padrão de aumento em cada linha (ex: 1º linha *, 2º linha **).

#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main()
{
  setlocale(LC_ALL, "Portuguese");
  int linhas;

  printf("Digite o número de linhas: ");
  scanf("%d", &linhas);

  for (int i = 1; i <= linhas; i++)
  {
    for (int j = 1; j <= i; j++)
    {
      printf("*");
    }
    printf("\n");
  }
  return 0;
}