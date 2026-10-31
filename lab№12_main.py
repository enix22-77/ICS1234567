import num_utils

num = int(input("Введіть ціле число: "))

max_d = num_utils.get_max_digit(num)
min_d = num_utils.get_min_digit(num)

print(f"Найбільша цифра: {max_d}")
print(f"Найменша цифра: {min_d}")
