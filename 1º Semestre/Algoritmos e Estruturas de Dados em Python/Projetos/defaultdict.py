from collections import defaultdict

# Cria um defaultdict que usará int() (retornando 0) para chaves novas
dd = defaultdict(int)

# Transforma a string em uma lista de palavras
words = 'data python data data structure data python'.split()

# Itera sobre cada palavra e incrementa seu contador no dicionário
for word in words:
  dd[word] += 1

# Imprime o resultado final após o loop terminar
print(dd)