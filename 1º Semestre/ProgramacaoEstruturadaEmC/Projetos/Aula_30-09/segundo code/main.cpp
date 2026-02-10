#include <stdio.h>

    int main(){

    int i = 2, tamanho = 3; // Declara a variavel i como inteiro e a variavel tamanho com o valor 3
    int vetor[tamanho]; // Declara um vetor com um tamanho definido pela variavel tamanho

    // Inicialização dos elementos do vetor
    vetor [0] = 1;
    vetor [1] = 2;
    vetor [2] = 3;

    // Loop para implimir os elementos do vetor
    for (i = 0; i < tamanho; i++){
        printf("%d ", vetor [i]);

    }
    return 0;
}
