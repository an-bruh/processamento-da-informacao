#Q2.py

def ordenador(vet):
  n = len(vet)
  m = int(n / 2)
  for i in range(m):
    if vet[i] < vet[n - 1 - i]:
      aux = vet[i]
      vet[i] = vet[n - 1 - i]
      vet[n - 1 - i] = aux

def saida(vet):
  texto =""
  for i in vet:
    texto += f"{i} "

  print(texto)

vet = [int(i) for i in input().split(' ') if i]
ordenador(vet)
saida(vet)