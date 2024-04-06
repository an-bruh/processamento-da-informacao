#Q2.py

def inversor(texto):
  invertido = ""
  comprimento = len(texto) - 1
  for i in range(comprimento, -1, -1):
   invertido += texto[i]

  return invertido 

a = input()
a = inversor(a)
b = input()
b = inversor(b)

print(f"{a}=2Vaj00={b}")