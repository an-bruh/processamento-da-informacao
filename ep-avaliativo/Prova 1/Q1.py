#Q1.py
#Link vídeo: https://youtu.be/iPSAJIskMwU

maiorSalario = idade25 = idade41 = somaSal = somaBonus = 0

def validaSalario(salario):
  while not(867 <= salario <= 20237):
    salario = int(input("Digite seu salario: "))
    
  return  salario

def validaIdade(idade):
  while not(15 <= idade <= 67):
    idade = int(input("Digite sua idade: "))
  
  return  idade

def verificaMaior(salario):
  global maiorSalario

  if salario > maiorSalario:
    maiorSalario = salario 

def funcionarioBetween(idade):
  global idade25
    
  if 20 <= idade <= 25:
    idade25 += 1

def funcionarioAcima(idade, salario):
  global somaSal, idade41

  if 41 < idade:
    idade41 += 1
    somaSal += salario

def calculaMedia():
  global somaSal, idade41
  media = 0

  if 0 < idade41:
    media = somaSal / idade41
  
  return media

def calculaBonus(salario):
  global somaBonus

  if salario < 1815:
    bonus = salario * 0.16
    somaBonus += bonus

def cadastraSalario():
  n = int(input())
  texto = "idade salario\n"
  for i in range(n):
    salario = int(input("Digite seu salario: "))
    salario = validaSalario(salario)
    idade = int(input("Digite sua idade: "))
    idade = validaIdade(idade)
    texto += f"{idade:-5}{salario:-8}\n"
    verificaMaior(salario)
    funcionarioBetween(idade)
    funcionarioAcima(idade, salario)
    calculaBonus(salario)

  return texto  

def saida(texto):
  media = calculaMedia()
  texto += f"\nmaior salario {'=':>28}{maiorSalario:-6}\n"
  texto += f"func. entre 20 e 25 anos {'=':>17}{idade25:-6}\n"
  texto += f"func. com mais de 41 anos {'=':>16}{idade41:-6}\n"
  texto += f"media dos sal. func. com mais de 41 anos ={media:-8.1f}\n"
  texto += f"bonus total {'=':>30}{somaBonus:-8.1f}\n"
  print(texto)

texto = cadastraSalario()
saida(texto)