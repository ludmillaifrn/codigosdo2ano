import math

def raizes(a, b, c):
  delta = b**2 - 4*a*c
  if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return x1, x2
  else:
    return None

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

resultado = raizes(a, b, c)

if resultado:
  print("As raízes são:", resultado)
else:
  print("Não existem raízes reais.")