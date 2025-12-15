from datetime import datetime
def format_date(date):
    return f"{date['ngay']}/{date['thang']}/{date['nam']}"
class Student:
    subject = "Python"
    def __init__(self, id, name, day_birth, score1, score2):
        self.id = id
        self.name = name
        self.day_birth = day_birth
        self.score1 = score1
        self.score2 = score2

    def score(self):
        return round((self.score1 + self.score2)/2, 2)

    def __str__(self):
        return f"{self.id:<7}{self.name:<20}{format_date(self.day_birth):<20}{self.score():<10}"

ids = set()
# Nhap
students = []
while True:
    id = input("Nhap id (Enter de dung): ")
    if id == "":
        break

    if id in ids:
        print("ID da ton tai, vui long nhap lai")
        continue
    name = input("Nhap name: ")
    ngay, thang, nam = map(int, input("Nhap ngay/thang/nam: ").split('/'))
    score1 = float(input("Nhap diem 1: "))
    score2 = float(input("Nhap diem 2: "))

    day_birth = {
        'ngay': ngay,
        'thang': thang,
        'nam': nam
    }

    ids.add(id)
    students.append(Student(id, name, day_birth, score1, score2))

# Sap xep tang dan theo ngay sinh (su dung key sort)
# students.sort(key=lambda sv: datetime(sv.day_birth['nam'], sv.day_birth['thang'], sv.day_birth['ngay']))

students.sort(key=lambda sv: datetime(sv.day_birth['nam'], sv.day_birth['thang'], sv.day_birth['ngay']))


print()
print(f"{'ID':<7}{'NAME':<20}{'DATE_BIRTH':<20}{'DTB':<10}")
for sv in students:
    print(sv)

    # 1. đầu -> ma trận
    # 2. oop