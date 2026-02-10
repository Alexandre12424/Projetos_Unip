#include <stdio.h>
float aplicar_desconto(float preco)
{
  preco = preco * 0.90; // Aplica 10% de desconto
  return preco;
}

int main()
{
  float valor = 100.0;
  float final = aplicar_desconto(valor);
  printf("Valor final: %.2f", final);
  // Qual o valor de 'valor' ao final da execucao?
  return 0;
}
