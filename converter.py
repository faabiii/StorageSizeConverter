import tkinter as tk
import tkinter.messagebox as msgbox

def convert_units():
    try:
        value = float(entry_value.get())
        source_unit = source_unit_var.get()
        target_unit = target_unit_var.get()

        # Umrechnungsfaktoren für verschiedene Speichergrößen
        conversion_factors = {
            "Byte": 1,
            "KiByte": 1024,
            "MiByte": 1024 ** 2,
            "GiByte": 1024 ** 3,
            "TiByte": 1024 ** 4,
            "KB": 1000,
            "MB": 1000 ** 2,
            "GB": 1000 ** 3,
            "TB": 1000 ** 4,
        }

        # Umrechnung von Quelleinheit zu Bytes
        bytes_value = value * conversion_factors[source_unit]

        # Umrechnung von Bytes zur Zieleinheit
        converted_value = bytes_value / conversion_factors[target_unit]

        result_label.config(text=f"{value} {source_unit} sind {converted_value} {target_unit}.")
    except ValueError:
        msgbox.showerror("Fehler", "Ungültige Eingabe!")

window = tk.Tk()
window.title("StorageSizeConverter")

label_value = tk.Label(window, text="Wert:")
label_value.grid(row=0, column=0, padx=10, pady=10, sticky="E")
entry_value = tk.Entry(window)
entry_value.grid(row=0, column=1, padx=10, pady=10)

label_source_unit = tk.Label(window, text="Quelleinheit:")
label_source_unit.grid(row=1, column=0, padx=10, pady=10, sticky="E")
source_units = ["Byte", "KiByte", "MiByte", "GiByte", "TiByte", "KB", "MB", "GB", "TB"]
source_unit_var = tk.StringVar()
source_unit_dropdown = tk.OptionMenu(window, source_unit_var, *source_units)
source_unit_dropdown.grid(row=1, column=1, padx=10, pady=10)

label_target_unit = tk.Label(window, text="Zieleinheit:")
label_target_unit.grid(row=2, column=0, padx=10, pady=10, sticky="E")
target_unit_var = tk.StringVar()
target_unit_dropdown = tk.OptionMenu(window, target_unit_var, *source_units)
target_unit_dropdown.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(window, text="Umrechnen", command=convert_units)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
