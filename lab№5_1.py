import math
x = float(input("Введіть x: "))
if x > 1:
    y = math.log10(abs(x + 1)) + 2.9 * math.exp(0.1 * x)
elif x > -1.1:
    y = math.sqrt(abs(x)) + x ** (1 / 3) - math.sin(x)
else:
    y = 4 * x + math.exp(x) - 4 * math.sqrt(abs(x))
print("y =", y)