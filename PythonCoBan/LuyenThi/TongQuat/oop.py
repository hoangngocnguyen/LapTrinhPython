class Person:
    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self.__age = age

    def __str__(self):
        return f"ID: {self._id}, NAME: {self._name}, AGE: {self.__age}"

    # Getter cho age
    @property
    def age(self):
        return self.__age
    # Setter cho age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Tuổi không được âm")
        self.__age = value


class Student(Person):
    def __init__(self, id, name, age, lop, truong):
        super().__init__(id, name, age)
        self.lop = lop
        self.truong = truong

    def __str__(self):
        return f"{super().__str__()}, TEST_ID: {self._id}, LOP: {self.lop}, TRUONG: {self.truong}"

    @staticmethod
    def is_pass_grade(grade):
        return grade >= 5

try:
    p1 = Person("1", "Hoang", 20)
    print(p1)
    p1.age = -2
    print(p1.age)
    s1 = Student("2", "Cindy", 18, "KTPM", "HUSC")
    print(s1)
    print(Student.is_pass_grade(6))
except ValueError as e:
    print(e)