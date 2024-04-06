area = 0 

def verificaPotencia():
  if (area < 10.9):
    print("Recomendamos 9000 BTU/h")
  elif (10.9 <= area < 15.9):
    print("Recomendamos 12000 BTU/h")
  elif (15.9 <= area < 20.9):
    print("Recomendamos 15000 BTU/h")
  elif (20.9 <= area < 25.9):
    print("Recomendamos 18000 BTU/h")
  elif (25.9 <= area <= 30.9):
    print("Recomendamos 21000 BTU/h")
  elif (area > 30.9):
    print("Sem recomendacao") 

area = float(input())

verificaPotencia()