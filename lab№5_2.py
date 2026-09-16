import math
xa = float(input("Введіть xA: "))
ya = float(input("Введіть yA: "))
xb = float(input("Введіть xB: "))
yb = float(input("Введіть yB: "))
xc = float(input("Введіть xC: "))
yc = float(input("Введіть yC: "))
A = math.sqrt(xa ** 2 + ya ** 2)
B = math.sqrt(xb ** 2 + yb ** 2)
C = math.sqrt(xc ** 2 + yc ** 2)
if A > B and A > C:
    print("Найбільша відстань у точки A")
elif B > A and B > C:
    print("Найбільша відстань у точки B")
else:
    print("Найбільша відстань у точки C")