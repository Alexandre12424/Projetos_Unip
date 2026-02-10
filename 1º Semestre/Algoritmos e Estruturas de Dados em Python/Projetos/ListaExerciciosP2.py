#Bubble sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

print("======================== Bubble Sort ========================")
valores = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", valores)
print("Lista ordenada:", bubble_sort(valores))

#Selection sort
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

print("\n======================== Selection Sort ========================")
valores = [64, 25, 12, 22, 11]
print("Lista original:", valores)
print("Lista ordenada:", selection_sort(valores))

#Insertion sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

print("\n======================== Insertion Sort ========================")
valores = [12, 11, 13, 5, 6]
print("Lista original: ", valores)
print("Lista ordenada: ", insertion_sort(valores))

#Merge sort
def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        L = lista[:mid]
        R = lista[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
    return lista

print("\n======================== Merge Sort ========================")
valores = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", valores)
print("Lista ordenada:", merge_sort(valores))

#Quick sort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2]
        left = [x for x in lista if x < pivot]
        middle = [x for x in lista if x == pivot]
        right = [x for x in lista if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
print("\n======================== Quick Sort ========================")
valores = [3,6,8,10,1,2,1]
print("Lista original:", valores)
print("Lista ordenada:", quick_sort(valores))
