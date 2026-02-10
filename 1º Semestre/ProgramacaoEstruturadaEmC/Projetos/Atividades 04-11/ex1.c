#include <stdio.h>
int main()
{
  // int tabuleiro;
  int i, j;
  for (i = 0; i < 3; i++)
  {
    for (j = 0; j < 3; j++)
    {
      if (i == j)
      {
        // tabuleiro[i][j] = 1; // Diagonal principal
      }
      else
      {
        // tabuleiro[i][j] = i + j;
      }
    }
  }
  // Qual é o valor armazenado em tabuleiro?

  // A declaração correta da variável tabuleiro é:
  // int tabuleiro[3][3];
  // Logo, não é possível armazenar um valor em tabuleiro sem especificar os índices.
  return 0;
}
