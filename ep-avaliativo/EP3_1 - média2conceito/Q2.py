# a função é definida aqui
def leia():
  a = float(input("Digite a 1a nota: "))
  b = float(input("Digite a 2a nota: "))
  return a, b;
# programa principal
# ENTRADA
nota1, nota2 = leia()
# PROCESSAMENTO E SAÍDA
media = (nota1 + nota2)/2
if media >= 9:  
  print("Conceito A")
elif media >= 7.5:  
  print("Conceito B");
elif media >= 6: 
  print("Conceito C")
elif media >= 5: 
  print("Conceito D")
else: 
  print("Reprovado! Conceito F")