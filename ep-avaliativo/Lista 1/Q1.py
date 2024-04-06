#Q1.py
tempo = int(input())

h = tempo / 3600
m = (h % 1) * 60
s = ((m % 1) * 60) + 0.1
 
print(f"{int(h):02d}:{int(m):02d}:{int(s):02d}")