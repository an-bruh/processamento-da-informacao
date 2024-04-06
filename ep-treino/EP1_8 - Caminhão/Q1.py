#EP1_8

carga = int(input())

carga500 = carga // 500
carga = carga % 500

carga100 = carga // 100
carga = carga % 100

carga25 = carga // 25
carga = carga % 25

carga1= carga // 1

print(f"{carga500}\n{carga100}\n{carga25}\n{carga1}")