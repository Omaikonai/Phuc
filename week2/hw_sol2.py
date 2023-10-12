class Warrior:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def show_info(self):
        hearts = '\u2665' * (self.health // 10)
        swords = '\u2694' * (self.strength // 10)
        print(f"Warrior {self.name} - Health: {hearts}, Strength: {swords}")

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name} with strength of {self.strength}!")
        enemy.got_hit(self.strength)

    def got_hit(self, damage):
        print(f"{self.name} got hit by {damage} damage!")
        self.health -= damage
        if self.health < 0:
            self.health = 0
        curr_health = '\u2665' * (self.health // 10)
        if self.health > 0:
            print(f"{self.name}'s current health is: {curr_health}")
        else:
            # using skull and crossbones for dead warriors
            print(f"{self.name} is dead \u2620")

# Testing
leo = Warrior("Leonidas", 100, 50)
xer = Warrior("Xerxes", 120, 40)

leo.show_info()   
xer.show_info()  

leo.attack(xer)   
xer.got_hit(leo.strength)   

xer.attack(leo)   
leo.got_hit(xer.strength)   
leo.got_hit(70)