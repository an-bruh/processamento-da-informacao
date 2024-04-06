#Q2.py
from math import sqrt

f = float(input())
h = float(input())

b = pow(f, 2) / (5 * sqrt(h * f))

print(f"B = {b:.03f}")