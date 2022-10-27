from ctypes.wintypes import WORD
import fixed_ingredients
import tkinter as tk

# This is code that creates the window for the app.

font_tuple_title = ("Comic Sans MS", 12, "bold")
font_tuple_text = ("Comic Sans MS", 10, "normal")
bg_color = "#b397be"  # #e5dce9

window = tk.Tk()
window.geometry("800x800")
window.configure(bg=bg_color)
window.title("Recipe Generator")

spacing = tk.Label(text="")
spacing.configure(bg=bg_color)
spacing.grid(column=0, row=0, rowspan=6, padx=95)

r_name = tk.Label(text=" Recipe Name: ")
r_name.configure(font=font_tuple_title, bg=bg_color)
r_name.grid(column=1, row=1)

r_name_entry = tk.Entry()
r_name_entry.configure(font=font_tuple_text, border=True, borderwidth=3)
r_name_entry.grid(column=1, row=2)

r_items = tk.Label(text=" Number of ingredients to use: ")
r_items.configure(font=font_tuple_title, bg=bg_color)
r_items.grid(column=1, row=3)

r_items_entry = tk.Entry()
r_items_entry.configure(font=font_tuple_text, border=True, borderwidth=3)
r_items_entry.grid(column=1, row=4)

textArea = tk.Text(master=window, height=30, width=50)
textArea.configure(font=font_tuple_text, border=True, borderwidth=3, wrap="word")
textArea.grid(column=1, row=6)

def make_recipe():
    textArea.delete("0.0", "end")
    name = r_name_entry.get()
    items = r_items_entry.get()

    try:
        items = int(items)
    except ValueError:
        items = 0

    resippy = fixed_ingredients.Recipe(name, items)
    
    textArea.insert(tk.END, resippy.format_recipe())

button = tk.Button(window, text="Generate Recipe", command=make_recipe, bg="#8a659f") # #916fa5
button.grid(column=1, row=5, pady=10)

window.mainloop()