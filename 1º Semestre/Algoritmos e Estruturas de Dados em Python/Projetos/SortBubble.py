# Define a função bubble_sort que recebe uma lista como argumento.
# O nome do argumento é 'lista' para não conflitar com a palavra-chave 'list' do Python.
def bubble_sort(lista):
    # Obtém o número de elementos na lista e armazena na variável 'n'.
    n = len(lista)
    # Loop externo que controla o número de "passadas" pela lista.
    # A cada passada completa, o maior elemento ainda não ordenado vai para sua posição final.
    for num_passada in range(n - 1):
        # Loop interno que faz as comparações e trocas.
        # Ele percorre a lista comparando cada elemento com o seu vizinho da direita.
        # O "- num_passada" é uma otimização, pois os últimos elementos já estão ordenados.
        for indice in range(n - num_passada - 1):
            # Compara o elemento atual com o próximo.
            if lista[indice] > lista[indice + 1]:
                # Se o elemento atual for maior que o próximo, troca-os de posição.
                # Esta é uma forma pythônica de fazer a troca de valores entre duas variáveis.
                lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]

# Cria uma lista vazia para armazenar os números do usuário.
numeros = []
print("Digite números para adicionar à lista. Digite 0 para parar.")

# Loop infinito para receber a entrada do usuário.
while True:
    try:
        # Pede ao usuário para digitar um número.
        entrada = input("Digite um número: ")
        # Converte a entrada (que é uma string) para um número inteiro.
        numero = int(entrada)

        # Se o número for 0, interrompe o loop.
        if numero == 0:
            break
        # Adiciona o número à lista.
        numeros.append(numero)

    except ValueError:
        # Se o usuário digitar algo que não é um número, avisa sobre a entrada inválida.
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Chama a função bubble_sort para ordenar a lista criada pelo usuário.
bubble_sort(numeros)
# Imprime a lista final, já ordenada.
print("\nA lista ordenada é:", numeros)
