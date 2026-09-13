import math

def calculate_fx(x):
    numerator = math.cos(x) + math.sin(2 * x)
    denominator = 42 * x
    result = (numerator / denominator) - math.log(abs(x + 1))
    return result

# Вказуємо значення x напряму у програмі
x_val = 2

y = calculate_fx(x_val)
print(f"Значення f({x_val}) = {y:.6f}")