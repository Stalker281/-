import tkinter as tk

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        output_label.config(text=f"Результат: {result}")
    except Exception as e:
        output_label.config(text=f"Ошибка: {e}")

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Рассчитать", command=calculate)
button.pack()

output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack()

root.mainloop()
