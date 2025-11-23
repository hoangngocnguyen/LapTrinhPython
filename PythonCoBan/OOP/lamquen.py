class Student:
    subject = 'Python'

    def __init__(self, id, name, score1, score2, score3):
        self.id = id
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def avg_score(self):
        return (self.score1 + self.score2 + self.score3) / 3

    def get_info(self):
        print(f"id: {self.id}, name: {self.name}, dtb: {self.avg_score()}")

sv1 = Student("1", "Hoàng", 9, 8, 7)
sv1.get_info()