e = int(input())
f = int(input())
d = int(input())

def calculaVox(e, f, d):
  vox = (e * pow(f, 2) * pow(d, 3)) / (e + f + d)

  return vox

print(f"vox = {calculaVox(e, f, d):.2f}")