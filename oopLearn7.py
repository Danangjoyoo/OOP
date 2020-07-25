class Hero:
    __count = 0
    def __init__(self, name):
        self.__name = name
        Hero.__count += 1
    @classmethod     #bisa dipanggil oleh objek maupun class (harus dengan self)
    def getCount(self):
        return self.__count

    @staticmethod    #bisa dipanggil oleh objek maupun class (tdk boleh dgn self
    def getCount1():
        return Hero.__count


axe = Hero('axe')
sven = Hero('sven')
print(Hero.getCount1())