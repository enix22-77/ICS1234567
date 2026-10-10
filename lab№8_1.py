import random
a = [random.randint(0, 15) for i in range(10)]
print("Початковий масив:")
print(a)
a.sort()
print("Відсортований масив:")
print(a)
a = a[5:] + a[:5]
print("Масив після обміну половин:")
print(a)C:\Users\dimak\OneDrive\Desktop\ICS_12\lab№7_1.py
