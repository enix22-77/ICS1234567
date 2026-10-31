import ast
import os

if not os.path.exists("islands.txt"):
    islands_data = {
        "Гренландія": 2130800,
        "Мадагаскар": 587041,
        "Калімантан": 748168,
        "Венкувер": 31788,
        "Ісландія": 103000,
        "Куба": 109884,
        "Ньюфаундленд": 111390,
        "Ірландія": 84421,
        "Сахалін": 76400,
        "Шпіцберген": 39044,
        "Цейлон": 65610,
        "Крит": 8336
    }
    with open("islands.txt", "w", encoding="utf-8") as f:
        f.write(str(islands_data))

with open("islands.txt", "r", encoding="utf-8") as f:
    islands = ast.literal_eval(f.read().strip())

name = input("Введіть назву острова: ")
square = float(input("Введіть площу острова у кв.км: "))
islands[name] = square

with open("dictionary.txt", "w", encoding="utf-8") as f:
    f.write(str(islands))

print("Дані успішно оновлено та збережено у файл dictionary.txt")
