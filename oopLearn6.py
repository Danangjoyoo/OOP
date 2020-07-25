import time

class Hero:
    global startTime
    __time = round(time.time(),2)
    __attackReceived = 0

    def __init__(self,name,damage,hp,armor,attackSpeed):
        self.__name = name
        self.__hp = hp
        self.__damage = damage
        self.__armor = armor
        self.__AS = attackSpeed
    #getter
    def getDamage(self):
        return self.__damage
    def getHP(self):
        return self.__hp
    def getArmor(self):
        return self.__armor
    def getAS(self):
        return self.__AS
    def getTime(self):
        return self.__time

    #setter
    def attack(self,enemy):
        self.updateTime()
        delta_Time = round((self.getTime() - startTime),2)
        time_Attack = round((delta_Time % self.getAS()),2)
        if time_Attack == 0:
            if (delta_Time/self.getAS()) > self.__attackReceived:
                enemy.attacked(self.__name,self.__damage)
                self.__attackReceived += 1
                print(self.__attackReceived)

    def attacked(self,enemy,damageDeliv):
        self.updateTime()
        self.__hp -= (damageDeliv/self.__armor)
        if self.__hp <= 0:
            print(self.__name + ' has been slain by ' + str(enemy))
        else:
            print(self.__name + ' attacked by ' + str(enemy) + ' | HP left: ' + str(round((self.__hp),2) ))
    def addDmg(self,addedDmg):
        self.__damage += addedDmg
    def addArmor(self,addedArmor):
        self.__armor += addedArmor
    def addAS(self,addedAS):
        self.__AS += addedAS
    def equip(self,weapon):
        if weapon.getDmgpoint() == True:
            self.addDmg(weapon.getDmgpoint())
        if weapon.getArmorpoint() == True:
            self.addArmor(weapon.getArmorpoint())
        if weapon.getAS() == True:
            self.addAS(weapon.getAS())
    def updateTime(self):
        self.__time = round(time.time(),2)

class weapon:
    def __init__(self,name,addDamage,addArmor,addAttackSpeed):
        self.__name = name
        self.__addDmg = addDamage
        self.__addArmor = addArmor
        self.__addAS = addAttackSpeed
    #getter
    def getDmgpoint(self):
        return self.__addDmg
    def getArmorpoint(self):
        return self.__addArmor
    def getAS(self):
        return self.__addAS


axe = Hero('axe',54,1100,5,1.25)
sven = Hero('sven',53,900,3,1.1)
sword = weapon('sword',50,0,-0.1)
kevlar = weapon('kevlar',0,11,0)
butterfly = weapon('butterfly',30,10,60)

sven.equip(butterfly)
startTime = round(time.time(),2)
i = 0
while True:
    universalTime = round(time.time(),2)
    i += 1
    #print('Time :', universalTime,' s')
    #print(time.time())
    sven.attack(axe)
    if axe.getHP() <= 0 or sven.getHP() <= 0:
        break

endTime = round(time.time(),2)
totalTime = round(endTime-startTime,2)
print('iterations', i, 'times')
print('Times Taken :', totalTime,'s')