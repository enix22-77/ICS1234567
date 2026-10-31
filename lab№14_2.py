
class HOME:
    def __init__(self, Address, Inhabitants, Square, Floors):
        self.Address = Address
        self.Inhabitants = Inhabitants
        self.Square = Square
        self.Floors = Floors

    def DisplayAll(self):
        print("Адреса:", self.Address)
        print("Мешканці:", self.Inhabitants)
        print("Площа:", self.Square, "м2")
        print("Кількість поверхів:", self.Floors)

    def SetSquare(self, square):
        self.Square = square

    def GetSquare(self):
        return self.Square

    def AddInhabitant(self, inhabitant):
        self.Inhabitants.append(inhabitant)

    def RemoveInhabitant(self, inhabitant):
        if inhabitant in self.Inhabitants:
            self.Inhabitants.remove(inhabitant)


home1 = HOME(
    "Київ, вул. Шевченка, 10",
    ["Іван", "Петро"],
    120,
    5
)

home2 = HOME(
    "Львів, вул. Франка, 15",
    ["Олена", "Марія"],
    200,
    9
)

home1.SetSquare(150)
home2.SetSquare(220)

home1.AddInhabitant("Андрій")
home2.AddInhabitant("Олександр")

print("БУДИНОК №1")
home1.DisplayAll()

print("\nБУДИНОК №2")
home2.DisplayAll()

print("\nПлоща першого будинку:", home1.GetSquare())
print("Площа другого будинку:", home2.GetSquare())
