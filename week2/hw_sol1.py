class Warrior:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def show_info(self):
        print(f"Warrior {self.name} - Health: {self.health}, Strength: {self.strength}")

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name} with strength of {self.strength}!")
        enemy.got_hit(self.strength)

    def got_hit(self, damage):
        print(f"{self.name} got hit by {damage} damage!")
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name}'s current health is: {self.health}")

# Testing
leo = Warrior("Leonidas", 100, 50)
xer = Warrior("Xerxes", 120, 40)

leo.show_info()   # Warrior Leonidas - Health: 100, Strength: 50
xer.show_info()   # Warrior Xerxes - Health: 120, Strength: 40

leo.attack(xer)   # Leonidas attacks Xerxes with strength of 50!
xer.got_hit(leo.strength)   # Xerxes got hit by 50 damage! Xerxes's current health is: 70

xer.attack(leo)   # Xerxes attacks Leonidas with strength of 40!
leo.got_hit(xer.strength)   # Leonidas got hit by 40 damage! Leonidas's current health is: 60

leo.got_hit(70)   # Leonidas got hit by 70 damage! Leonidas's current health is: 0
