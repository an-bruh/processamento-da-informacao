#Q4.py

def calculaMedia(x):
  soma = 0
  d = len(x)
  for i in x:
    soma += i
  media = soma / d

  return media

def calculaHagrid(x):
  med = calculaMedia(x)
  soma = 0
  n = len(x)
  for i in range(n):
    arit = (2 * (((2 * x[i]) - (3 * med)) ** 2)) * 4 * x[i]
    soma += arit
  hagrid = ((3 / (2 * (n ** 2))) * soma) ** (1/2)

  return hagrid

vet = [float(i) for i in input().split(' ') if i]
print(f"{calculaHagrid(vet):.2f}")