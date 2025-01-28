class SettingsManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.settings = {}

    def load_settings(self):
        try:
            with open(self.file_path, "r") as f:
                lines = f.readlines()
                for line in lines:
                    key, value = line.strip().split(":")
                    self.settings[key.strip()] = value.strip()
            print("Nastavení načteno úspěšně.")
        except FileNotFoundError:
            print("Soubor nenalezen. Vytvářím nový soubor pro nastavení.")

    def save_settings(self):
        with open(self.file_path, "w") as f:
            for key, value in self.settings.items():
                f.write(f"{key} : {value}\n")
            print("Nastavení uloženo úspěšně.")

    def set_setting(self, key, value, replace_existing=True):
        if replace_existing or key not in self.settings:
            self.settings[key] = value
            print(f"Nastavení {key} nastaveno na {value}.")
        else:
            print(f"Klíč {key} již existuje. Chcete nahradit existující hodnotu?")

            user_input = input("Zadejte 'ano' pro nahrazení, nebo 'ne' pro přidání nové hodnoty: ").lower()
            if user_input == "ano":
                self.settings[key] = value
                print(f"Nastavení {key} bylo nahrazeno hodnotou {value}.")
            elif user_input == "ne":
                print(f"Nastavení {key} zůstalo nezměněno.")
            else:
                print("Neplatný vstup. Nastavení zůstalo nezměněno.")

    def get_setting(self, key):
        return self.settings.get(key, "Nastavení nenalezeno.")

# Použití
file_path = r"C:\Users\danie\Desktop\Python\text\test.txt"
manager = SettingsManager(file_path)
manager.load_settings()

# Uživatelský vstup pro nastavení s možností nahrazení existující hodnoty
keys = ["pozdrav", "loučení", "jiné"]
for key in keys:
    value = input(f"Zadejte hodnotu pro {key}: ")
    replace_existing = input(f"Chcete nahradit existující hodnotu pro {key}? (ano/ne): ").lower() == "ano"
    manager.set_setting(key, value, replace_existing)

# Uložení nastavení
manager.save_settings()

# Získání hodnoty
for key in keys:
    value = manager.get_setting(key)
    print(f"{key}: {value}")
