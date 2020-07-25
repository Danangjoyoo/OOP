class Hero:
    __count = 0
    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp
        Hero.__count += 1
    @classmethod     #bisa dipanggil oleh objek maupun class (harus dengan self)
    def getCount(self):
        return self.__count

    @staticmethod    #bisa dipanggil oleh objek maupun class (tdk boleh dgn self
    def getCount1():
        return Hero.__count

    @property
    def hp(self):
        return self.gethp

    @hp.setter
    def hp(self, addedHP):
        self.__hp += addedHP

    @hp.getter
    def gethp(self):
        return self.__hp

axe = Hero('axe',1100)
print(axe.gethp)
axe.hp = 100
print(axe.hp)

