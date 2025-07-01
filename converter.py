import tkinter as tk
from tkinter import ttk

UNITS = [
    "Meters",
    "Centimeters",
    "Kilometers",

    "Yards",
    "Inches",
    "Miles"
]

UNIT_TO_METER = {
    "Meters" : 1.0, # 1 meter = 1 meter
    "Centimeters" : 0.01, # 1 cm = 0.01 meters
    "Kilometers" : 1000.0, # 1 km = 1000 meters

    "Yards" : 0.9144, # 1 yard = 0.9144 meters
    "Inches" : 0.0254, # 1 inch = 0.0254 meters
    "Miles" : 1609.34 # 1 mile = 1609.34 meters
}

def convert():
    unit_from = selected_unit.get()
    unit_to = unit_to_convert_to.get()
    value = current_value.get()

    print(f"Convert {value} {unit_from} to {unit_to}.")

    try:
        base = float(value)

        # convert 'from' to meters first
        meters = base * UNIT_TO_METER[unit_from]
        result = meters / UNIT_TO_METER[unit_to]

        result_var.set(f"{value} {unit_from.lower()} is about {result} {unit_to.lower()}.")
    except ValueError:
        result_var.set("Invalid input.")

def on_entry_change(*args):
    value = current_value.get()

    try:
        base = float(value)

        button.pack()
    except ValueError:
        button.pack_forget()

root = tk.Tk()
root.title("Unit converter")
root.geometry("300x300")
root.resizable(False, False) # not resizable in x or y

selected_unit = tk.StringVar(value="Meters") # variable class for this specific library
unit_to_convert_to = tk.StringVar(value="Kilometers")
current_value = tk.StringVar(value=10)
current_value.trace_add("write", on_entry_change)

style = ttk.Style()
style.theme_use("clam")

entry = ttk.Entry(root, textvariable=current_value)
entry.pack(pady=10)

from_text = ttk.Label(root, text="From:")
from_text.pack()

convert_from = ttk.Combobox(root, values=UNITS, state="readonly", textvariable=selected_unit)
convert_from.pack(pady=2)

to_text = ttk.Label(root, text="To:")
to_text.pack()

convert_to = ttk.Combobox(root, values=UNITS, state="readonly", textvariable=unit_to_convert_to)
convert_to.pack(pady=2)

button = ttk.Button(root, text="Convert", command=convert, width=len("Convert"))
button.pack(pady=10)

result_var = tk.StringVar() # no value by default

result_label = tk.Label(root, textvariable=result_var)
result_label.pack(pady=10)

root.mainloop()
