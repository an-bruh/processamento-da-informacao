import math
texto = ""

def criaLista():
  listatemp = []
  verific95 = True
  while verific95:
    temp = int(input())
    if temp != 95:
      listatemp.append(temp)
    else:
      verific95 = False
      
  return listatemp
  

def verificaTemp(texto, listatemp):
  cont14, between, cont26, temps, d = 0, 0, 0, 0, 0
  for temp in listatemp:
    temps += temp
    d += 1
    if temp < 14:
      cont14 += 1
    if 14 <= temp < 26:
      between += 1
    if 26 <= temp:
      cont26 += 1
  media = temps / d

  texto += f"número de dias em que a temperatura esteve abaixo de 14C = {cont14}\n"
  texto += f"número de dias em que a temperatura esteve entre 14C e 26C = {between}\n"
  texto += f"número de dias em que a temperatura esteve acima de 26C = {cont26}\n"
  texto += f"média das temperaturas em todo o período considerado = {media:.2f}\n"

  return texto

def encontraMediana(texto, listatemp):
  cop = listatemp.copy()
  for i in range(len(cop)):
    for j in range(i, len(cop)):
      if cop[i] > cop[j]:  
        T = cop[i]
        cop[i] = cop[j]
        cop[j] = T    
  if len(cop) % 2 != 0:      
    indice = math.ceil(len(cop) / 2)
    mediana = cop[indice-1]
  else:
    indice = math.ceil(len(cop) / 2)
    mediana = (cop[indice - 1] + cop[indice]) / 2
  
  texto += f"temperatura do 2o quartil calculada = {mediana:.2f}\n"

  return texto, mediana

def temperaAcima(texto, listatemp, mediana):
  for i in range(len(listatemp)):
    if mediana <= listatemp[i]:
      texto += f"temperatura acima do 2o quartil medida no dia {i + 1} foi de {listatemp[i]}C\n"

  return texto    

listatemp = criaLista()
texto = verificaTemp(texto, listatemp)
texto, mediana = encontraMediana(texto, listatemp)
texto = temperaAcima(texto, listatemp, mediana)

print(texto)  