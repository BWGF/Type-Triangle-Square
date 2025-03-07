import tkinter as tk
import tkinter.font as font
import Square

def calculate_square():
    a = int(entry_a.get())
    result = Square.square(a, a, a, a)
    result_label.config(text=f"Результат: {result}")

root = tk.Tk()
root.title("Квадрат")
root.geometry("400x300")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (300 / 2)
y = (screen_height / 2) - (300 / 2)
root.geometry(f"+{int(x)}+{int(y)}")

font_style = font.Font(size=13)

entry_a = tk.Entry(root)
entry_b = tk.Entry(root)
entry_c = tk.Entry(root)
entry_d = tk.Entry(root)
result_label = tk.Label(root, text="Результат: ")
calculate_button = tk.Button(root, text="Рассчитать", command=calculate_square)
label_a = tk.Label(root, text="Сторона a: ", font=font_style)
label_b = tk.Label(root, text="Сторона b: ", font=font_style)
label_c = tk.Label(root, text="Сторона c: ", font=font_style)
label_d = tk.Label(root, text="Сторона d: ", font=font_style)

label_a.place(relx=0.3, rely=0.1, anchor="e")
entry_a.place(relx=0.45, rely=0.1, anchor="center")
label_b.place(relx=0.3, rely=0.2, anchor="e")
entry_b.place(relx=0.45, rely=0.2, anchor="center")
label_c.place(relx=0.3, rely=0.3, anchor="e")
entry_c.place(relx=0.45, rely=0.3, anchor="center")
label_d.place(relx=0.3, rely=0.4, anchor="e")
entry_d.place(relx=0.45, rely=0.4, anchor="center")
calculate_button.place(relx=0.5, rely=0.5, anchor="center")
result_label.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()
