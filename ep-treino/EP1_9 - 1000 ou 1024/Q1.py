#EP1_9

valor = int(input())

valorgb = valor * (10 ** 9)
valorgib = valor * (2 ** 30)

dif = valorgib - valorgb

print(f"{valorgb}\n{valorgib}\n{dif}\n")