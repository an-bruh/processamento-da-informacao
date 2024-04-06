#Q4.py

def lerMatriz():
  import numpy as np
  m, ler_linha = [], input()
  while ler_linha:
    m.append([int(i) for i in ler_linha.split(' ') if i])
    ler_linha = input()
  return (np.array(m)).tolist()

def calculaSomaCasas(tabuleiro):
  casaspretas = 0
  casasbrancas = 0

  for i in range(2):
    for j in range(i, len(tabuleiro), 2):
      for k in range(len(tabuleiro[j])):
        if k % 2 == 0:
          if tabuleiro[j][k] % 2 == 0:
            if i % 2 == 0:
              casaspretas += tabuleiro[j][k]
            else:
              casasbrancas += tabuleiro[j][k] 
        else:
          if tabuleiro[j][k] % 2 == 0:
            if i % 2 == 0:
              casasbrancas += tabuleiro[j][k]
            else:
              casaspretas += tabuleiro[j][k]
  
  return casaspretas, casasbrancas           
        
tabuleiro = lerMatriz()
casaspretas, casasbrancas = calculaSomaCasas(tabuleiro)
print(f"soma pares na cor=3 é {casasbrancas}; e na outra cor é {casaspretas}")      