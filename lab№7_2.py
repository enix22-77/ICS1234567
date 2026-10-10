import random
s = int(input("Введіть кількість номерів: "))
for i in range(s):
    ccc = random.randint(100, 999)
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    n3 = random.randint(0, 9)
    n4 = random.randint(0, 9)
    n5 = random.randint(0, 9)
    n6 = random.randint(0, 9)
    n7 = random.randint(0, 9)
    phone = f"+999-{ccc}-{n1}{n2}{n3}-{n4}{n5}-{n6}{n7}"
    print(phone)
