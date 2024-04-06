from math import sqrt

p2x = int(input())
p2y = int(input())

def calcula_distancia_Manhattan(p2x, p2y):

  p1x = 19
  p1y = -11

  dist = sqrt((p2x-p1x)**2 +(p2y-p1y)**2)
  
  return dist

print(f"distancia Manhattan = {calcula_distancia_Manhattan(p2x, p2y):.2f}")