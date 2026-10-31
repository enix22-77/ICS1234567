population = {
    "Ukraine": 41000000,
    "France": 67000000,
    "Poland": 38000000
}

area = {
    "Ukraine": 603628,
    "France": 551695,
    "Poland": 312696
}

country = input("Введіть назву країни для пошуку: ")
if country in population and country in area:
    print(f"Країна: {country}")
    print(f"Населення: {population[country]}")
    print(f"Площа: {area[country]} кв. км")
else:
    print("Країну не знайдено.")

new_country = input("\nВведіть назву нової країни для додавання: ")
new_pop = int(input("Введіть населення: "))
new_area = float(input("Введіть площу (кв. км): "))

population[new_country] = new_pop
area[new_country] = new_area

print("\nОновлені словники:")
print("Населення:", population)
print("Площа:", area)
