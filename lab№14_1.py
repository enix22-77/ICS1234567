
class PLANE:
    def __init__(self, model, firm, year, speed):
        self.model = model
        self.firm = firm
        self.year = year
        self.speed = speed

    def ChangeSpeed(self, speed):
        self.speed = speed


planes = [
    PLANE("Boeing 737", "Boeing", 2020, 800),
    PLANE("Airbus A320", "Airbus", 2022, 850),
    PLANE("Boeing 777", "Boeing", 2021, 900)
]

print("СПИСОК ЛІТАКІВ")

for plane in planes:
    print("Модель:", plane.model)
    print("Фірма:", plane.firm)
    print("Рік випуску:", plane.year)
    print("Швидкість:", plane.speed, "км/год")
    print("----------------------")

planes[0].ChangeSpeed(950)

print("Нова швидкість першого літака:",
      planes[0].speed, "км/год")
