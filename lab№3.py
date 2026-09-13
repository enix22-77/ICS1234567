number = int(input("Введіть трицифрове число: "))
digit3 = number % 10
digit2 = (number // 10) % 10
digit1 = number // 100
reserved_number = digit3 * 100 + digit2 * 10 + digit1
print("Число у зворотньому порядку:", reserved_number)