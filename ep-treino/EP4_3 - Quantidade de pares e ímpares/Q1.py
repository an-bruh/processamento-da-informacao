#EP4_3
def leiaValores(n):
  v = []
  for i in range(n):
    valor = int(input())
    v.append(valor)

  return v

def contaParesImpares(v):
  par = 0
  impar = 0
  for i in range(len(v)):  
    if (v[i] % 2) == 0:
      par += 1
    else:
      impar += 1

  print(par, impar)       

n = int(input())
vetor = leiaValores(n)
contaParesImpares(vetor)