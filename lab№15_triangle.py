import tkinter as tk
import math

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a <= 0 or b <= 0 or c <= 0:
            result.config(text="Сторони повинні бути додатними!")
            return

        if a + b <= c or a + c <= b or b + c <= a:
            result.config(text="Трикутник не існує!")
            return

        perimeter = a + b + c

        p = perimeter / 2

        area = math.sqrt(p * (p-a) * (p-b) * (p-c))

        result.config(
            text="Периметр: " + str(round(perimeter, 2)) +
            "\nПлоща: " + str(round(area, 2))
        )

    except ValueError:
        result.config(text="Введіть правильні числа!")


window = tk.Tk()
window.title("Трикутник")
window.geometry("350x300")

tk.Label(window, text="Сторона A:").pack()
entry_a = tk.Entry(window)
entry_a.pack()

tk.Label(window, text="Сторона B:").pack()
entry_b = tk.Entry(window)
entry_b.pack()

tk.Label(window, text="Сторона C:").pack()
entry_c = tk.Entry(window)
entry_c.pack()

button = tk.Button(
    window,
    text="Обчислити",
    command=calculate
)
button.pack(pady=10)

result = tk.Label(window, text="Результат з'явиться тут")
result.pack()

window.mainloop()
