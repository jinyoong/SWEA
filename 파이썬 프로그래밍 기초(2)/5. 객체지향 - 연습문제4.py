class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def area(self):
        return 3.14 * self.radius ** 2

r = Circle(2)
print("원의 면적: {:0.2f}".format(r.area()))