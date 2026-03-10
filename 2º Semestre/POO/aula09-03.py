matriz = [[0]*4 for _ in range(3)]

print(matriz)

num = 0

for i in range(3):
  for j in range(4):
      num += 1
      matriz[i][j] = num
        
print(matriz)

if i == 0 and j ==3:
    print("Matriz após preenchida a primeira linha: ")
for linha in matriz:
    print(linha)
print()

print("Matriz totalmente preenchida: ")
for linha in matriz:
    print(linha)
    print()

matriz[0][0] = matriz[2][3]

print("Matriz após copiar o último valor para a primeira posição: ")
for linha in matriz:
    print(linha)
