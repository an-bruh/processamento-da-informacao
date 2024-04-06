def verificaNumero():
  for x in range(0, 5):
    n = float(input())
    if n > 107:
      print("Meta atingida")
      break
    else:  
      print("Insuficiente")

verificaNumero()