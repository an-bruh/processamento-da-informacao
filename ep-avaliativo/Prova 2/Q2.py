#Q2.py

def abreFecha(texto):
  abriu = 0
  fechou = 0
  for i in range(1, len(texto) + 1):
    n = i - 1
    if texto[n:i] == "{":
      abriu += 1
    if texto[n:i] == "}":
      fechou += 1   
  return abriu, fechou    

texto = input()  
abriu, fechou = abreFecha(texto)
if abriu == fechou:
  print("Igual abre/fecha { e }")
else:  
  print("Erro abre/fecha { e }")