def testaPremiacao():
  premio = 7672
  premiop = premio
  total = 0
  qmais = 0
  qsetor6 = 0
  percent = 0

  texto = "valor tent1 tent2 total qmais qsetor6 premio\n"

  while premio >= 0:
    valor = int(input())
    tent1 = int(input())
    tent2 = int(input())
    if (valor > 102):
      if (tent1 == 6 or tent2 == 6):
        qsetor6 += 1
      if (tent1 == 6):
        premio -= 539  
      if (tent1 + tent2) > 11:
        qmais += 1 
        premio -= 816
      texto += "%5d %5d %5d %5d %5d %7d %6d\n" % (valor, tent1, tent2, total, qmais, qsetor6, premio)    
      total += 1        
  percent = (qmais / total) * 100  
  texto += f"\nPremio = {premiop}\nTotal de participantes = {total}\n"
  texto += f"Clientes acertaram 6 na 1a tent. = {qsetor6}\nPorcentagem Clientes acertaram mais que 11 = {percent:.1f}"

  print(texto)

testaPremiacao()