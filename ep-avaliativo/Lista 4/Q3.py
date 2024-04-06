def testaPremiacao():
  premio = 7672
  total = 0
  qmais = 0
  qsetor6 = 0

  texto = "valor tent1 tent2 total qmais qsetor6 premio\n"

  while premio >= 0:
    valor = int(input())
    tent1 = int(input())
    tent2 = int(input())
    if (valor > 102):
      total += 1
      if (tent1 == 6):
        qsetor6 += 1
        premio -= 539 
      if (tent1 + tent2) > 11:
        qmais += 1 
        premio -= 816
    texto += "%5d %5d %5d %5d %5d %7d %6d\n" % (valor, tent1, tent2, total, qmais, qsetor6, premio)

  print(texto)

testaPremiacao()