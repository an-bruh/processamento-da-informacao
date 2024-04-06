#Q4.py

def lerMatriz():
  import numpy as np
  m, ler_linha = [], input()
  while ler_linha:
    m.append([int(i) for i in ler_linha.split(' ') if i])
    ler_linha = input()
  return (np.array(m)).tolist()

def verificaPermutavel(m):
  for j in range(len(m[0])):
    existe = [False]*len(m)
    for i in range(len(m)):
      for x in range(len(m)):
        if m[i][j] == x:
          existe[x] = True
    for a in existe:
      if not a:
        return "NAO"
  return "SIM" 

m = lerMatriz()

print(verificaPermutavel(m))    