import random

def generate_serial():
    letter = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    number = random.randint(10000, 99999)
    return f"{letter}-{number}"

n = int(input("Введіть кількість серійних номерів N: "))
serials = [generate_serial() for _ in range(n)]

print("Згенеровані серійні номери:")
for s in serials:
    print(s)
