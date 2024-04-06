# a função é definida aqui
def delta( a, b, c ):
  d = b * b - 4 * a * c;
  return d;
# agora já pode ser usada
valor = delta( 5, -2, 4)
print("O delta de 5x^2 – 2x + 4 é %.1f" % valor)