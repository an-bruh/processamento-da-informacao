#Q1.py
#Link video: https://youtu.be/x48cHYj9Mbc
def lerMatriz():
  import numpy as np
  m, ler_linha = [], input()
  while ler_linha:
    m.append([int(i) for i in ler_linha.split(' ') if i])
    ler_linha = input()
  return (np.array(m)).tolist()

def encontraIndice(m):
  indice = -1

  for i in range(len(m)):
    if m[i][7] == 5:
      indice = i
      break

  print(indice)

m = lerMatriz()
encontraIndice(m)