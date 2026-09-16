import math
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))
n = int((b - a) / h) + 1
for i in range(n):
    x = a + i * h
    if x >= 0:
        y = math.sqrt(x) / (3 + abs(math.sin(x)))
        print(f"x = {x:.2f}, y = {y:.4f}")