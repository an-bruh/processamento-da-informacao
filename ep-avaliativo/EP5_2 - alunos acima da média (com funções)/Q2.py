import numpy as np # muito útil para trabalhar com vetor!
# MÉTODO(S)
def leia(n):
  v = np.zeros(n).astype(int) # aloca vetor de inteiro com n elementos
  for i in range(n):
    v[i] = int(input())
  return v
# ENTRADA DE DADOS
n = int(input("Digite o numero de alunos:"))
print("Entre com " + str(n) + " RAs:")
ras = leia(n)
print("Entre com " + str(n) + " Notas:")
notas = leia(n)
# PROCESSAMENTO
somador = 0
for i in range(n):
  somador += notas[i]
media = somador/n
contador = 0
for i in range(n):
  if notas[i] >= media:
    contador += 1
# SAÍDA DE DADOS
print("Média da turma =", media) 
print("Número de alunos acima da média =", contador)
print("LISTA DE ALUNOS ACIMA DA MÉDIA")
print("RA\t Nota")
for i in range(n):
  if notas[i] >= media:    
    print(ras[i],"\t",notas[i])