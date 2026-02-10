#include <stdio.h>
#include <stdlib.h>

int main()
{
    int notas [5]; //declarando um vetor com 5 indice

    //Preenchendo o vetor
    for(int i = 0; i < 5; i++){
        printf("Digite a nota %d ", i + 1);
        scanf("%d", &notas[i]);
    }

    //acessando e imprimindo
    for (int i = 0; i < 5; i++){
        printf("Nota na pisição %d: %d\n", i + 1, notas[i]);
    }

    return 0;
}
