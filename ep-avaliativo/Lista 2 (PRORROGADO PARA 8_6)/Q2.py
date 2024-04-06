valor = int(input())

def calculaDinheiro(valor):

  tret40 = valor // 40
  valor = valor % 40

  tret27 = valor // 27
  valor = valor % 27

  tret24 = valor // 24
  valor = valor % 24

  tret11 = valor // 11
  valor = valor % 11

  tret1 = valor // 1

  return tret40, tret27, tret24, tret11, tret1

tret40, tret27, tret24, tret11, tret1 = calculaDinheiro(valor)

print(f"{tret40} TretaCoin(s) de OZ$ 40 \n{tret27} TretaCoin(s) de OZ$ 27 \n{tret24} TretaCoin(s) de OZ$ 24 \n{tret11} TretaCoin(s) de OZ$ 11 \n{tret1} TretaCoin(s) de OZ$ 1")