#Q1.py
#Link vídeo: https://youtu.be/onW7pKtQX_I
import numpy as np

def escreverMatriz(m):
  print("Matriz espiral horária passo 3:")
  for linha in m:
    print(*linha)

def trataEntrada():
  vet = [str(i) for i in input().split('Linha=') if i]
  for i in vet:
    a = i
    vet2 = [int(i) for i in a.split('Coluna=') if i]

  return vet2  

def matrizEspiral(vet):
  l = vet[0]
  c = vet[1]
  m = np.zeros((l, c)).astype(int)
  cont = 0
  ini = 0
  fimc = c - 1
  fiml = l - 1
  while (cont < l*c):
    for i in range(ini, fimc + 1):
      m[ini][i] = cont * 3
      cont += 1
    if (cont >= l * c):
      break
    for i in range(ini + 1,  fiml + 1):
      m[i][fimc] = cont * 3
      cont += 1
    if (cont >= l * c):
      break  
    for i in range(fimc - 1, ini - 1, -1):
      m[fiml][i] = cont * 3
      cont += 1 
    if (cont >= l * c):
      break   
    for i in range(fiml - 1, ini, -1):
      m[i][ini] = cont * 3
      cont += 1   

    ini += 1;
    fiml -= 1;
    fimc -= 1;  

  escreverMatriz(m)

vet = trataEntrada()
matrizEspiral(vet)