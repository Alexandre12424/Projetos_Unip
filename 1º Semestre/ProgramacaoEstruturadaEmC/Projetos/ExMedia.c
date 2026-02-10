#include <stdio.h>
#include <locale.h>

int main()
{
  setlocale(LC_ALL, "Portuguese");

  float nota1, nota2, media;

  printf("Digite a primeira nota: ");
  scanf("%f", &nota1);

  printf("Digite a segunda nota: ");
  scanf("%f", &nota2);

  media = (nota1 + nota2) / 2.0;

  printf("Média: %.2f\n", media);

  if (media >= 6.0)
  {
    printf("situação: Aprovada\n");
  }
  else
  {
    printf("Situação: Reprovada\n");
  }

  return 0;
}