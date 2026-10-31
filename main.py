from home_module import HOME

house1 = HOME("вул. Хрещатик, 1", 120.5, 2)
house2 = HOME("вул. Шевченка, 10", 85.0, 1)

house1.AddInhabitant("Олександр")
house1.AddInhabitant("Марія")

house2.AddInhabitant("Іван")

house2.SetSquare(90.0)

print("=== Будинок 1 ===")
house1.DisplayAll()
print(f"Отримана площа через GetSquare: {house1.GetSquare()} кв. м\n")

print("=== Будинок 2 ===")
house2.DisplayAll()
print(f"Отримана площа через GetSquare: {house2.GetSquare()} кв. м")
