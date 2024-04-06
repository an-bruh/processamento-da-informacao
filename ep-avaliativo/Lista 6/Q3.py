#Q3.py

y = [3.3, 0.8, 3.2, 1.9, 2.7, 2.5, 4.2, 1.6, 0.9, 3.3, 2.7, 0.0, 3.4, 1.6, 2.2, 1.1, 2.2, 1.1]

def calculaConvolucao(x):
  soma = 0
  n = len(x)
  for i in range(n):
    convolacao = (1/7) * (i + 1) * x[i] * y[n - i - 1]
    soma += convolacao
  
  return soma

vet = [float(i) for i in input().split(' ') if i]
print(f"{calculaConvolucao(vet):.2f}")