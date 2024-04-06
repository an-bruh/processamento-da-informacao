def encontraMenor(A, B, C):
  T = 0
  if (A > B):
    T = A
    A = B
    B = T
  if (A > C):
    T = A
    A = C
    C = T
  if (B > C):
    T = B
    B = C
    C = T

  print(A)
    
A, B, C = int(input()), int(input()), int(input())

encontraMenor(A, B, C)