#Q1.py
#Link video: https://youtu.be/_wJ8jjdlpKc 

def preencheVetor(vet):
  E2 = [0]*22
  n = 1
  m = 0

  for i in range(2):
    if vet[0] > vet[n] and vet[0] > vet[21]:
      E2[m] = vet[0]
    elif vet[n] > vet[21]:
      E2[m] = vet[n]
    else:
      E2[m] = vet[21]
    n += 19
    m += 21 

  for j in range(1, 21):
    if vet[j] > vet[j + 1] and vet[j] > vet[j - 1]:
      E2[j] = vet[j]
    elif vet[j + 1] > vet[j - 1]:
      E2[j] = vet[j + 1]
    else:
      E2[j] = vet[j - 1]

  return E2

def saida(vet):
  texto =""
  for i in vet:
    texto += f"{i} "

  print(texto)  


E1 =  [int(i) for i in input().split(' ') if i]
E2 = preencheVetor(E1)
saida(E2)