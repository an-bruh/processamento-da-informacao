#Q4.py

def calculaFuncao(x):
  f = 0
  
  if 2 <= x < 4:
    f = (x - 2) ** 2 + 1
  elif 4 <= x < 7:
    f = 1 - (x - 4) ** 2 - 2
  elif x < 2 or x > 7: 
    f = 2

  return f

def saida(x):
  print(f"f({x}) = {calculaFuncao(x)}")

x = int(input()) 
saida(x) 