def convert_units(value, source_unit, target_unit):
    try:
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

        return converted_value
    except KeyError:
        return None

units = ["Byte", "KiByte", "MiByte", "GiByte", "TiByte", "KB", "MB", "GB", "TB"]

unit_string = ", ".join(units)
source_unit = input(f"Wähle die Quelleinheit ({unit_string}): ")
target_unit = input(f"Wähle die Zieleinheit ({unit_string}): ")
value = float(input("Gib den umzurechnenden Wert ein: "))

result = convert_units(value, source_unit, target_unit)

if result is not None:
    print(f"{value} {source_unit} sind {result} {target_unit}.")
else:
    print("Ungültige Auswahl oder Umrechnung nicht möglich.")
