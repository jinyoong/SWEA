class Student:
    def __init__(self, kor, eng, mat):
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat

    @property
    def kor(self):
        return self.__kor

    @property
    def eng(self):
        return self.__eng

    @property
    def mat(self):
        return self.__mat

    def total_score(self):
        return self.__kor + self.__eng + self.__mat


s_k, s_e, s_m = map(int, input().split(", "))
student = Student(s_k, s_e, s_m)
print("국어, 영어, 수학의 총점: {}".format(student.total_score()))