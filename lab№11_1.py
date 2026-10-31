import csv

num = int(input("Введіть натуральне число: "))
divisors = []

for i in range(1, num + 1):
    if num % i == 0:
        divisors.append([i])

with open("div.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Divisor"])
    writer.writerows(divisors)

print(f"Дільники числа {num} збережено у div.csv")
