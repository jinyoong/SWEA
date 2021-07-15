# 중요!! 오버라이딩 문제다

class Shape:
    def area(self):
        return 0

class Square(Shape):

    def __init__(self, length):
        self.__length = length

    # 부모 클래스인 Shape를 상속받았지만
    # area 함수를 재정의하여 사용한다.
    def area(self):
        return self.__length ** 2

x= Square(3)
print("정사각형의 면적: {}".format(x.area()))