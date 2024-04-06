#Link video: https://youtu.be/k3YWR12c7JM
#Q1.py

def geraVetor():
  vet = [float(i) for i in input().split(' ') if i]

  return vet

def calculaProduto(a, b):
  somaProduto = 0
  for i in range(21):
    produto = a[i] * b[i]
    somaProduto += produto

  return somaProduto

a = geraVetor()
b = geraVetor()

produto = calculaProduto(a, b)

print(f"{produto:.2f}")