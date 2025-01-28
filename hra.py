import random

# Definování postav
class Character:
    def __init__(self, name, health, mana, stamina):
        self.name = name
        self.health = health
        self.mana = mana
        self.stamina = stamina

    def attack(self, enemy):
        if self.stamina > 0:
            damage = random.randint(10, 20)
            enemy.health -= damage
            self.stamina -= 10
            print(f"{self.name} zaútočil a způsobil {damage} poškození!")
        else:
            print(f"{self.name} nemá dostatek výdrže k útoku!")

    def magic_attack(self, enemy):
        if self.mana > 0:
            damage = random.randint(15, 25)
            enemy.health -= damage
            self.mana -= 10
            print(f"{self.name} použil magii a způsobil {damage} poškození!")
        else:
            print(f"{self.name} nemá dostatek many k útoku!")

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        player.health -= damage
        print(f"{self.name} zaútočil a způsobil {damage} poškození!")

# Vytvoření postav
characters = {
    "Kouzelník": Character("Kouzelník", health=80, mana=100, stamina=50),
    "Bojovník": Character("Bojovník", health=100, mana=30, stamina=100),
    "Tank": Character("Tank", health=150, mana=20, stamina=120)
}

# Vytvoření nepřítele
enemy = Enemy("Goblin", health=100, attack_power=15)

# Výběr postavy hráče
print("Vyber si postavu:")
for char_name in characters:
    print(char_name)

choice = input("Zadej název postavy: ")
player = characters.get(choice)

if not player:
    print("Neplatná volba! Zvolili jsme za tebe Bojovníka.")
    player = characters["Bojovník"]

# Hlavní cyklus hry
while player.health > 0 and enemy.health > 0:
    print(f"\n{player.name} - Životy: {player.health}, Mana: {player.mana}, Výdrž: {player.stamina}")
    print(f"{enemy.name} - Životy: {enemy.health}")
    
    print("1. Útok (výdrž)")
    print("2. Magický útok (mana)")
    action = input("Zvol akci (1/2): ")
    
    if action == "1":
        player.attack(enemy)
    elif action == "2" and player.name == "Kouzelník":
        player.magic_attack(enemy)
    else:
        print("Neplatná volba!")
    
    if enemy.health > 0:
        enemy.attack(player)

# Výsledek
if player.health > 0:
    print(f"Gratuluji! {player.name} porazil {enemy.name}.")
else:
    print(f"{enemy.name} tě porazil.")
