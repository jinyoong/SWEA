class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return "이름: {}".format(self.name)

# Student 클래스를 상속받는다.
# 이름은 그대로 받아오면 되니까 전공 관련 코드만 작성하면 될듯?
class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.__major = major

    @property
    def major(self):
        return self.__major

    def __repr__(self):
        return super().__repr__() + ", 전공: {}".format(self.major)


a = Student("홍길동")
b = GraduateStudent("이순신", "컴퓨터")
print(a)
print(b)