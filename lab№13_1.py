planes = [
    PLANE("Boeing 737", "Boeing", 2015, 850),
    PLANE("A320", "Airbus", 2018, 830),
    PLANE("AN-148", "Antonov", 2012, 800)
]

print("Початковий список літаків:")
for plane in planes:
    print(plane)

planes[0].set_speed(900)

print("\nПісля зміни швидкості першого літака:")
for plane in planes:
    print(plane)
