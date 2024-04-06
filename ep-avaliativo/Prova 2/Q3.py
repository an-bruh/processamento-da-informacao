#Q3.py

def lerMatriz():
  import numpy as np
  m, ler_linha = [], input()
  while ler_linha:
    m.append([int(i) for i in ler_linha.split(' ') if i])
    ler_linha = input()
  return (np.array(m)).tolist()

def criaLista(m):
  lista = []
  for i in (range(len(m))):
    lista.append(m[i][0])
  
  return lista  

def mudaPosicao(vetor):
  for i in range(len(vetor)):
    for j in range(i, len(vetor)):
      if vetor[i] > vetor[j]:  
        T = vetor[i]
        vetor[i] = vetor[j]
        vetor[j] = T

  return vetor

def permutaColuna(v, m):
  for j in range(1,len(m[0])):
    temp = []
    if j % 2 == 0:
      for i in range(len(m)):
        temp.append(m[i][j])
      temp = mudaPosicao(temp)
      for i in range(len(v)):
        if temp[i] != v[i]:
          return "Permutações Colunas Pares = NAO"
  return "Permutações Colunas Pares = SIM"     
 



m = lerMatriz()
vet = criaLista(m)
vet = mudaPosicao(vet)
print(permutaColuna(vet, m))