// Enunciado:
// Desenvolvam um programa em C que colete o nome, idade e três notas de um aluno.
// Calcule a média aritmética das notas.
// Exiba uma mensagem personalizada sobre o desempenho do aluno com base na média (Aprovado com excelente desempenho se >=9, Aprovado se >=7 e <9, Reprovado se <7)
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

float calcularMedia(float n1, float n2, float n3)
{
  return (n1 + n2 + n3) / 3;
}

int main()
{
  setlocale(LC_ALL, "Portuguese");

  char nome[100];
  int idade;
  float resultado, n1, n2, n3;

  printf("Digite seu nome: ");
  scanf(" %s", nome);

  printf("Digite sua idade: ");
  scanf("%d", &idade);

  printf("Digite sua primeira nota: ");
  scanf("%f", &n1);
  printf("Digite sua segunda nota: ");
  scanf("%f", &n2);
  printf("Digite sua terceira nota: ");
  scanf("%f", &n3);

  resultado = calcularMedia(n1, n2, n3);

  //(Aprovado com excelente desempenho se >=9, Aprovado se >=7 e <9, Reprovado se <7)
  if (resultado >= 9)
  {
    printf("Parabéns %s! \n Você foi aprovado com média: %.2f um excelente desempenho! \n E lembre-se você tem apenas %d anos, continue assim!", nome, resultado, idade);
  }
  else if (resultado >= 7)
  {
    printf("Parabéns %s! \nVocê foi aprovado com média: %.2f, um bom desempenho! \n E lembre-se você tem apenas %d anos, continue estudando pra melhorar cada vez mais!", nome, resultado, idade);
  }
  else
  {
    printf("Infelizmente %s você foi reprovado com média: %.2f! \n Lembre-se você tem apenas %d anos, estude mais para conseguir melhorar sua nota!", nome, resultado, idade);
  }
  return 0;
}
