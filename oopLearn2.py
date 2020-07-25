class Hero:
    hero_count = 0
    def __init__(self,inpName,inpDmg,inpHP):
        self.name = inpName
        self.damage = inpDmg
        self.HP = inpHP
        Hero.hero_count += 1

    #method tanpa return, tanpa argumen
    def who(self):
        print("My Name is " + self.name)

    #method dengan argumen, tanpa return
    def HP_Up(self,up):
        self.HP += up

    #method with return
    def getHP(self):
        return self.HP

hero1 = Hero('Sven',55,500)
hero2 = Hero('axe',67,1100)

hero1.who()
hero1.HP_Up(200)

print(hero1)