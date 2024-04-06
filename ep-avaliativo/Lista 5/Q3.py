#Q3.py

def removedor(texto):
  removido = ""
  for i in range(len(texto)):
    if texto[i] not in 'aeiouAEIOU':
      removido += texto[i]

  return removido

texto = input()
texto = removedor(texto)

print(f"{texto}EFFF3tpmzw")