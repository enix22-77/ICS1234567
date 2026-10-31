import random
colors = ("red", "green", "blue", "yellow", "orange", "purple", "pink")
fruits = ("apple", "banana", "cherry", "orange", "grape", "peach", "pear")
n = int(input("Введіть кількість словосполучень N: "))
for i in range(n):
    color = random.choice(colors)
    fruit = random.choice(fruits)
    print(f"{i + 1}. {color} {fruit}")
