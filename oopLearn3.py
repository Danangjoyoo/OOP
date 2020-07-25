class Hero:
    hurt = False
    def __init__(self,name,hp,damage,armor):
        self.name = name
        self.__hp = hp
        self.__damage = damage
        self.__armor = armor
        

    def attack(self,enemy):
        hurt = True
        print(self.name + ' attacking ' + str(enemy) )
        enemy.attacked(self.name,self.__damage,hurt)

    def attacked(self,enemy,damage,hurt):
        if hurt == True:
            self.__hp = round((self.__hp - damage / self.__armor),2)
            print(self.name + ' attacked by ' + str(enemy))
            print(self.name + ' s hitpoints left: ' + str(self.__hp))
            if self.__hp <= 0:
                self.dead(enemy)
        elif hurt == False:
            self.__hp = self.__hp
            print(str(enemy) + ' attack is blocked by ' + self.name)
    def dead(self, enemy):
        print(self.name + ' has been slain by ' + str(enemy))

    def gethp(self):
        return self.__hp

sniper = Hero('sniper',550,45,4)
axe = Hero('axe',1100,48,2)

while True:
    if str(input('command: ')) == 'a':
        sniper.attack(axe)
    else:
        None
    if axe.gethp() <= 0:
        break
