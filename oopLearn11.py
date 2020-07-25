from abc import ABC, abstractmethod

class temen(ABC):
    __counter = 0
    def __init__(self,nama,umur):
        self.__name = nama
        self.__age = umur
        self.__score = 1

    @property
    @abstractmethod
    def score(self):
        return self.__score

    @abstractmethod
    def ngobrol(self):
        return print("ngobrol sama temen")

    @abstractmethod
    def curhat(self):
        return print('curhat sama temen')

class sahabat(temen):
    def ngobrol(self):
        self.score = 1
        return print("ngobrol sama sahabat")

    @temen.score.getter
    def score(self):
        return self.__score
    
    @score.setter
    def score(self,val):
        self.__score += val

    @abstractmethod
    def curhat(self):
        self.score = 1
        return print('sahabat curhat')


class pacar(sahabat):
    def ngobrol(self):
        self.score = 1
        return print("ngobrol sama pacar")
    def curhat(self):
        return sahabat.curhat(self)
    def mesra(self):
        self.score = 1

revina = pacar("revina",22)
revina.curhat()