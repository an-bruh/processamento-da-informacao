#Q3.py

def lerMatriz():
  import numpy as np
  m, ler_linha = [], input()
  while ler_linha:
    m.append([int(i) for i in ler_linha.split(' ') if i])
    ler_linha = input()
  return (np.array(m)).tolist()

def verificaUm(m):
  cont = 0

  for i in range(len(m)):
    for j in range(len(m[0])):
      if m[i][j] == 1:
        cont += 1
        break
  if cont == len(m):
    print("SIM")
  else:
    print("NAO")

m = lerMatriz()
verificaUm(m)