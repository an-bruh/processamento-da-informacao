#Q4.py
B = "87"

def contaOcorrencias(texto):
  ocorrencia = 0
  for i in range(len(B), len(texto) + 1):
    n = i - len(B)
    if texto[n:i] == B:
      ocorrencia += 1
  return ocorrencia    

texto = input()  
n = contaOcorrencias(texto)

print(f"O texto {B} ocorre {n} vez(es) na entrada lida.")