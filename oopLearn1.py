class Hero:
    #class variable / static variable
    count = 0
    def __init__(self,inputName,inputDamage,inputHP,inputMP):
        # Instance Variable (Hanya dimiliki si Hero) / Attribut
        self.name = inputName
        self.damage = inputDamage
        self.HP = inputHP
        self.MP = inputMP
        Hero.count += 1
        print("Creating Hero: ", inputName)


hero1 = Hero("Sniper",120,1000,130)
hero2 = Hero("sven",150,3000,100)
print(Hero.count)
#print(Hero.__dict__)

"""hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper"
hero1.hp = 100

hero2.name = "sven"
hero2.hp = 1000

hero3.name = "axe"
hero3.hp = 2000

print(hero1)
print(hero1.__dict__)
print(hero1.name)"""