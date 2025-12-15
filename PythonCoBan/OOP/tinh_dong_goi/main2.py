class Student:
    subject = "Python"
    def __init__(self, id, name, score1, score2):
        self.id = id
        self.name = name
        self.__score1 = score1
        self.__score2 = score2

    def __avg_score(self):
        return round((self.__score1 + self.__score2) / 2, 2)

    def DTB(self):
        return self.__avg_score()

    # @property
    # def a(self):
    #     return self.__avg_score()




sv = Student("1", "Cindy", 6.7, 9.8)

print(f"{sv.id}, {sv.name}, {sv.DTB()}")

# Cach khonog khuyen kich
print(sv._Student__score1)