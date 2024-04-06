#EP4_2
def leiaValores(n):
  v = []
  a = []
  for i in range(n):
    nome = input()
    a.append(nome)
    valor = float(input())
    v.append(valor)
    
  return v, a

def calculaMedia(v):
  somaNota = 0
  for i in range(len(v)):
    somaNota += v[i]
  media = somaNota / len(v)  

  return media

def encontraAcima(m, v, n):
  contador = 0
  for i in range(len(v)):
    if v[i] > m:
      contador += 1
      print(n[i])

  return contador

n = int(input())
notas, nomes = leiaValores(n)
media = calculaMedia(notas)
acima = encontraAcima(media, notas, nomes)