acumulador, contador = 0,0
print("Entre com 10 notas válidas")
while (contador<10):
  nota = float(input())
  if nota<0 or nota>10:
    continue
  acumulador += nota
  contador += 1

media = acumulador/contador

# SAÍDA
print("A média das " + str(contador) + " notas é " + str(round(media,1)));