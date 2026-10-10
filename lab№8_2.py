a = []
for i in range(3):
    row = list(map(int, input("Введіть числа через пробіл: ").split()))
    a.append(row)
s = 0
for i in range(3):
    for j in range(len(a[i])):
        if (i + j) % 2 != 0:
            s += a[i][j]
print("Двовимірний масив:")
for row in a:
    print(row)
print("Сума елементів:", s)
