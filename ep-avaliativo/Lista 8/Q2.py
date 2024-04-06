#Q2.py
def lerMatriz():
  import numpy as np
  m, ler_linha = [], input()
  while ler_linha:
    m.append([int(i) for i in ler_linha.split(' ') if i])
    ler_linha = input()
  return (np.array(m)).tolist()

def calculaSoma(m):
  soma = 0
  for i in range(len(m)):
    for j in range(len(m[0])):
      if 0 <= j - i and j < len(m) - i:
        if m[i][j] % 2 != 0:
          soma += m[i][j]
  print(f"soma ímpares triângulo superior é {soma}")

m = lerMatriz()
calculaSoma(m)  