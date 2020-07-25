class Hero:
    heroes_count = 0
    __jumlah = 0

    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

        #private instance's variable
        self.__anjay = 'anjay1'

        #protected
        self._protected = 'protected'

axe = Hero('axe',1100)

print(Hero.__dict__)