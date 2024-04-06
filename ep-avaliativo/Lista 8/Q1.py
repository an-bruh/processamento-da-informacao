#Q1.py
#Link vídeo: https://youtu.be/ZrpdKbhagLM
import numpy as np

def escreverMatriz(m):
  for linha in m:
    print(*linha)

def lerMatriz():
  import numpy as np
  m, ler_linha = [], input()
  while ler_linha:
    m.append([int(i) for i in ler_linha.split(' ') if i])
    ler_linha = input()
  return (np.array(m)).tolist()
  
def mediaVizinhos(m):
  for i in range(len(m)):
    for j in range(len(m[0])):
      soma = 0
      d = 0
      media = 0
      for viz_i in range(-1, 2):
        for viz_j in range(-1, 2):
          if 0 <= i + viz_i < len(m) and 0 <= j + viz_j < len(m[0]):
            soma += m[i+viz_i][j+viz_j]
            d += 1  
      media = round(soma / d)
      r[i][j] = media

  escreverMatriz(r)  

m = lerMatriz()

r = np.zeros((len(m),len(m[0]))).astype(int)

mediaVizinhos(m)