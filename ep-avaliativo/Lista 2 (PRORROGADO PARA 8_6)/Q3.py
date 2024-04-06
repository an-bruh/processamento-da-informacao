x = 22

y = int(input())
z = int(input())

def  calcula_menor(e, f):
  menor = (e + f - abs(e - f)) / 2
  
  return menor

res = calcula_menor(y, z)
final = calcula_menor(res, x)

print(f"O menor inteiro: {final:.0f}")