#include <stdio.h>
#include <stdlib.h>

float subtrair(float n1, float n2)
{
  return n1 - n2;
}

float somar(float a, float b)
{
  return a + b;
}

float multiplicar(float a, float b)
{
  return a * b;
}

float dividir(float a, float b)
{
  return a / b;
}

int main()
{
  float n1 = 0, n2 = 0;
  printf("Hello World!");
  printf("\nDigite o primeiro numero: ");
  if (scanf("%f", &n1) != 1)
  {
    printf("Erro: Entrada invalida. Por favor, insira um numero.\n");
    return 1;
  }

  printf("Digite o segundo numero: ");
  if (scanf("%f", &n2) != 1)
  {
    printf("Erro: Entrada invalida. Por favor, insira um numero.\n");
    return 1;
  }

  printf("Resultado da soma dos dois numeros: %f", somar(n1, n2));
  printf("\nResultado da subtracao dos dois numeros: %f", subtrair(n1, n2));
  printf("\nResultado da multiplicacao dos dois numeros: %f", multiplicar(n1, n2));
  printf("\nResultado da divisao dos dois numeros: %f", dividir(n1, n2));

  return 0;
}