class Student:
    subject = "Python"
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.__score = score

    def __str__(self):
        return (f"{self.id}, {self.name}, {self.__score}")

    # C1:
    def getScore(self):
        return self.__score
    def setScore(self, score):
        self.__score = score


    # C2:
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score



sv = Student("1", "Cindy", 6.7)

print(sv)

print(sv.name)
sv.score = 8.6
# sv.setScore(9.4)
# print(sv.getScore(), sv.score)


print(sv)

print(sv.score, sv.getScore())

"""
    dung annotaton; @property: phuong thuc trar ve thuoc tinh
    @nam.setter
    
    thi o duoi co quyen truy xuat den private.
    Ban chat no la mot method
"""

