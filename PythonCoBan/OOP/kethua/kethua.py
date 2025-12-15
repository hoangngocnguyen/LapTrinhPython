class Person:
    def __init__(self, id, name, address):
        # protected property
        self._id = id
        self._name = name
        self._address = address

    def __str__(self):
        return f"ID: {self._id}, NAME: {self._name}, ADDRESS: {self._address}"
class Student(Person):
    def __init__(self, id, name, address, score):
        super().__init__(id, name, address)
        self.__score = score

    def __str__(self):
        return f"{super().__str__()}. SCORE: {self.__score}"
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score


st1 = Student("1", "Hoàng", "Hue", 9)

st1.score = 123
print(st1, st1.score)
