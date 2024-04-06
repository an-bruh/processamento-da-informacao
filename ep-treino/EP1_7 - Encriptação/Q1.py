#EP1_7

n = input()
r = ""

for i in range(len(n)):
  if n[i] == "9":
    r += "0"
  else:
    r += str(int(n[i]) + 1)

print(r)