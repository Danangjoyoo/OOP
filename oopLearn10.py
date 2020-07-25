#INHERIT SUPER-SUBB (TAK SETARA)
class Hero: #Tingkat 1
    def __init__(self,name,hp):
        self.__name = name
        self.__hp = hp

    def getHP(self):
        return self.__hp

class Hero_INT(Hero): #Tingkat 2
    def __init__(self,name,hp):
        super().__init__(name,hp)

    def getHP(self):
        return super().getHP()

class human(Hero_INT): #Tingkat 3
    def __init__(self,name,hp):
        super(Hero_INT, self).__init__(name,hp)
#        indeks super(<diisi mau diambil dari induk yg mana>, self)

class ogre(Hero_INT): #Tingkat 3
    def __init__(self,name,hp):
        super().__init__(name,hp)

#MULTIPLE INHERIT SETARA
class minuman: #Tingkat 1
    def setVolume(self,addVolume):
        self.__volume = addVolume
    def getVolume(self):
        return self.__volume

class makanan: #Tingkat 1
    def setMass(self,addMass):
        self.__mass = addMass
    def getMass(self):
        return self.__mass

class energen(minuman,makanan): #Tingkat 2
    def __init__(self,mass,volume):
        super().setMass(mass)
        super().setVolume(volume)

lina = human('lina',500)
magi = ogre('magi',1200)
print(lina.getHP())
print(magi.getHP())

milo = energen(500,10)
milo.setMass(123)
print(milo.getMass())
milo.setVolume(1000)
print(milo.getVolume())

help(milo)