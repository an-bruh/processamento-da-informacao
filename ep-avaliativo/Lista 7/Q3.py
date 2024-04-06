#Q3.py

def escreverMatriz(m):
  for linha in m:
    print(*linha)

def geradorMatriz(dimensoes):
  import numpy as np
  m = np.zeros((dimensoes[0],dimensoes[1])).astype(int)
  for i in range(len(m)):
    for j in range(len(m[i])):
      m[i][j] = (2 * i + 2 * j) % 9

  return m    

dimensoes = [int(i) for i in input().split(' ') if i]
m = geradorMatriz(dimensoes)
escreverMatriz(m)