class square():
    def __init__(self, garo, sero):
        self.__garo = garo
        self.__sero = sero

    @property
    def garo(self):
        return self.__garo

    @property
    def sero(self):
        return self.__sero

    def area(self):
        return self.garo * self.sero

x = square(5, 4)

print("사각형의 면적: {}".format(x.area()))