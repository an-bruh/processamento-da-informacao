#Link vídeo: https://youtu.be/cJsgeNS_cX0 


x, y, efic, qtdl = 0, 0, 0, 0

def distEuclidiana():
  dist = (pow(x, 2) + pow(y, 2)) ** (1 / 2)

  return dist

def verificaQtdLitros():
  if (dist <= (efic * qtdl)):
    print("S")
  else:
    print("N")

x, y, efic, qtdl = float(input()), float(input()), float(input()), float(input())

dist = distEuclidiana()
verificaQtdLitros()