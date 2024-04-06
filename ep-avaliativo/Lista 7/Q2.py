#Q2.py

def lerMatriz():
  import numpy as np
  m, ler_linha = [], input()
  while ler_linha:
    m.append([int(i) for i in ler_linha.split(' ') if i])
    ler_linha = input()
  return (np.array(m)).tolist()

def calculaInfSomaPrinc(m):
  somaPrinc = 0

  for i in range(len(m)):
    for j in range(len(m[i])):
      if i > j:
        if m[i][j] % 2 == 0:
          somaPrinc += -(m[i][j])
  return somaPrinc          

m = lerMatriz()
print(f"multiplicação abaixo pares = {calculaInfSomaPrinc(m)}")