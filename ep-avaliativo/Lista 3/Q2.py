a, b, c = 0, 0, 0

def verificaTriangulo():
  abq = pow(a, 2) + pow(b, 2)
  cq = pow(c, 2)

  if (abq > cq):
    print("A")
  elif (abq == cq):
    print("R")
  elif (abq < cq):
    print("O")

a, b, c = int(input()), int(input()), int(input())

verificaTriangulo()