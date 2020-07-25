import time

class Hero:
    global startTime
    __time = round(time.time(),3)

    def __init__(self,name,HP,damage,armor):
        self.__name = name
        self.__damage = damage
        self.__baseDmg = damage
        self.__armor = armor
        self.__baseArmor = armor
        self.__hp = HP
        self.__baseHP = HP
        self.__exp = 0
        self.__level = 1
        self.__reqExp = 1000
        self.__deadState = False
        self.__resTime = 0
        self.__deadTime = 0

    #STAT
    def stats(self):
        print(self.name, 'stats:' )
        print('damage :',self.damage)
        print('armor  :',self.armor)
        print('HP     :',self.hp)

    #NAME
    @property
    def name(self):
        return self.__name

    #LEVEL
    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, CurrentExp):
        print('CurrentExp :',CurrentExp)
        if CurrentExp >= self.__reqExp:
            self.__level += 1
            self.__exp = 0
            self.levelUp()
            self.NewReqExp(self.level)
    def levelUp(self):
        self.armor = self.level
        self.damage = self.level
        self.hp = self.level
        print(self.__name, 'got Level Up! to level', self.level)

    #HP
    @property
    def hp(self):
        return round(self.__hp,0)
    @hp.setter
    def hp(self, level):
        self.__hp = self.__baseHP*(1 + 0.01*level)

    #DAMAGE
    @property
    def damage(self):
        return round(self.__damage,0)
    @damage.setter
    def damage(self, level):
        self.__damage = self.__baseDmg * (1 + 0.01*level)

    #ARMOR
    @property
    def armor(self):
        return round(self.__armor,0)
    @armor.setter
    def armor(self, level):
        self.__armor = self.__baseArmor * (1 + 0.01*level)

    #METHODS
    def attack(self, enemy):
        enemy.attacked(self, self.damage)

    def attacked(self, enemy, damage):
        now_Time = round(time.time(),3)
        delta_Time = round(now_Time - self.__deadTime,3)
        self.__hp -= damage / self.armor
        if (delta_Time - self.resTime) >= 0:
            if self.__hp <= 0:
                if self.dead == False:
                    enemy.getExp(self)
                    enemy.kill(self)
                    self.dead = True
                    print(self.dead)
                elif self.dead == True:
                    enemy.resTime = enemy.level
            else:
                print('{} attacked by {}'.format(self.__name, enemy.name))
                print('{} HP left: {}'.format(self.__name, self.hp))
        else:
            self.dead = False
            self.hp = self.level


    #DEAD
    @property
    def dead(self):
        return self.__deadState
    @dead.setter
    def dead(self, status):
        self.__deadState = status
        self.__deadTime = time.time()

    #RESURRECTION TIME
    @property
    def resTime(self):
        return self.__resTime
    @resTime.setter
    def resTime(self, level):
        self.__resTime = round(level*5,2)


    def kill(self,enemy):
        print('{} has been slain by {}'.format(enemy.name,self.__name))

    def getExp(self, enemy):
        self.__exp += (enemy.level * 1000)
        self.level = self.__exp

    def NewReqExp(self, level):
        self.__reqExp += self.__reqExp * (1 + 0.01*level)

startTime = time.time()

axe = Hero('axe',1100,43,3)
sven = Hero('sven',900,54,5)
sniper = Hero('sniper',550,47,5)
lina = Hero('lina',570,48,1)

print(sven.stats())
i = 0
while True:
    i += 1
    while axe.dead == False:
        i += 1
        sven.attack(axe)
        #print(axe.dead)
        if axe.dead == True:
            break
    while sniper.dead == False:
        i += 1
        sven.attack(sniper)
        if sniper.dead == True:
            break
    while lina.dead == False:
        i += 1
        sven.attack(lina)
        if lina.dead == True:
            break
    if lina.dead == True and axe.dead == True and sniper.dead == True:
        break

print(sven.stats())
print('iteration takes: {}'.format(i))