#Link vídeo: https://youtu.be/_VzNq_JFDss

def calculaImunidade(p, TxContagio):
  i = 0
  Cti = 1426
  somaCti = Cti

  while (p * 0.61) >= somaCti:
      Cti = Cti * TxContagio
      somaCti += Cti
      i += 1
      print(Cti)

  return i

p = int(input())
TxContagio = float(input())

print(f"A cidade conseguiu imunidade coletiva em {calculaImunidade(p, TxContagio)} dias")