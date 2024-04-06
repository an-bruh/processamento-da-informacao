#EP4_1
def leiaValores(n):
  v = []
  for i in range(n):
    valor = int(input())
    v.append(valor)

  return v

def encontraMaior(v):
  maior = 0
  for i in range(len(v)):
    if v[i] > maior:
      maior = v[i]

  return maior

   
n = int(input())
vetor = leiaValores(n)
maior = encontraMaior(vetor)

print(maior)