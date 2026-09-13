import math

def calculate_V(a, b, h, x, y):
    return (1 / 3) * a * b * h * math.cos(x) + math.log(y)

if __name__ == "__main__":
    print("Результат Завдання 2:", calculate_V(2.0, 3.0, 4.0, 0.5, 5.0))