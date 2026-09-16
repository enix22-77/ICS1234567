import math
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))
spisok = []
x = a
while x <= b:
    if x >= 0:
        y = math.sqrt(x) / (3 + abs(math.sin(x)))
        spisok.append(y)
    x += h
print("Список:")
print(spisok)
zeros = spisok.count(0)
print("Кількість нулів:", zeros)
if len(spisok) >= 2:
    sorted_list = sorted(enumerate(spisok), key=lambda item: item[1])
    print("Індекс першого найменшого:", sorted_list[0][0])
    print("Індекс другого найменшого:", sorted_list[1][0])