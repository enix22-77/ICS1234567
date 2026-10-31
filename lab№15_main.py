import tkinter as tk
import json
import os

window = tk.Tk()
window.title("Жорсткі диски")
window.geometry("300x210")
window.configure(bg="gray")

label = tk.Label(
    window,
    text="Список жорстких дисків",
    bg="gray"
)
label.grid(row=0, column=0)

text = tk.Text(window, width=35, height=9)
text.grid(row=1, column=0, padx=5, pady=5)

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "input.json"
)

try:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    for disk in data["disks"]:
        text.insert(
            tk.END,
            disk["model"] + " — " + str(disk["price"]) + " грн\n"
        )

except Exception as error:
    text.insert(tk.END, "Помилка: " + str(error))

window.mainloop()
