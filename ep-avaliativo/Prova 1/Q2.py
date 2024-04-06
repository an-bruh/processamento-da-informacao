#Q2.py

x = 67
y = 38

def achaTesouro():
  while True:
    xe = int(input())
    ye = int(input())
    if (xe == x and ye == y):
      print("Acertou")
      break
    else:
      print("Errou")

achaTesouro()