def cadastraPedido():
  texto = ""
  qtd = 0
  qtdp = 0
  valorp = 0
  media = 0
  sumbonus = 0
  qtddisc = 0

  while True:
    desc = 0.0
    linha = int(input())
    if linha != 0:
      qtd += 1
      valor = int(input())
      regiao = int(input())
      if linha == 6:
        if regiao == 9:
          bonus = valor * 0.08 
          desc = valor * 0.03 
        else: 
          bonus = valor * 0.05
          desc = valor * 0.06
          sumbonus += bonus
        texto += f"Linha: {linha} Pedido: {valor:.1f} Regiao: {regiao} Desconto: {desc:.1f} Bonus: {bonus:.1f}\n"
      else:
        if regiao == 9 and valor >= 400:
          desc = valor * 0.1
        else:
          qtddisc += 1
        texto += f"Linha: {linha} Pedido: {valor:.1f} Regiao: {regiao} Desconto: {desc:.1f}\n"
      if 200 <= valor <= 400:
        qtdp += 1
        valorp += valor
        media = valorp / qtdp
    else:
      break
  texto += f"Quantidade de pedidos: {qtd}\nValor medio de pedidos entre 200 e 400 reais: {media:.1f}\n"
  texto += f"Soma dos bonus de pedidos da regiao 7: {sumbonus:.1f}\nQuandidade de pedidos sem descontos: {qtddisc}"      
  print(texto)

cadastraPedido()