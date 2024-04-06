#Q3.py

def verificaPotencia(area):
  if (area < 11.4):
    texto = "Recomendamos 9800 BTU/h"
  elif (11.4 <= area < 16.4):
    texto = "Recomendamos 12800 BTU/h"
  elif (16.4 <= area < 21.4):
    texto = "Recomendamos 15800 BTU/h"
  elif (21.4 <= area < 26.4):
    texto = "Recomendamos 18800 BTU/h"
  elif (26.4 <= area <= 31.4):
    texto = "Recomendamos 21800 BTU/h"
  elif (area > 31.4):
    texto = "Sem recomendacao"

  return texto  

def saida(area):
  print(f"Para area = {area} : {verificaPotencia(area)}")

area = float(input())

saida(area)