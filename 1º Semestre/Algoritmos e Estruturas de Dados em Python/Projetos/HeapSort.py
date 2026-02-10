def heapify(arr, n, i):
    largest = i  # Inicializa o maior como raiz
    l = 2 * i + 1  # filho da esquerda = 2*i + 1
    r = 2 * i + 2  # filho da direita = 2*i + 2

    # Se o filho da esquerda existe e é maior que a raiz
    if l < n and arr[i] < arr[l]:
        largest = l

    # Se o filho da direita existe e é maior que o maior até agora
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Se o maior não é a raiz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca
        # Heapify recursivamente a subárvore afetada
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Constrói um max-heap.
    # Começa do último nó pai e vai até a raiz.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai elementos um por um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move a raiz atual para o final
        heapify(arr, i, 0)  # Chama max heapify no heap reduzido

# Exemplo de uso:
lista_numeros = [12, 11, 13, 5, 6, 7]
print("Lista original:", lista_numeros)
heap_sort(lista_numeros)
print("Lista ordenada (Heap Sort):", lista_numeros)