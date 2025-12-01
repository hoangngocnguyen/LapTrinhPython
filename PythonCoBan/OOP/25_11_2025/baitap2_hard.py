from datetime import datetime

def format_date(date):
    return f"{date['ngay']}/{date['thang']}/{date['nam']}"
class Student:
    subject = "Python"

    def __init__(self, id, name, score1, score2, date_of_birth):
        self.id = id
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.date_of_birth = date_of_birth

    def score(self):
        return round((self.score1 + self.score2) / 2)

    def __str__(self):
        return f"{self.name:<15}; {format_date(self.date_of_birth):<15}; {self.score():<10}"

    # Qúa tải cho < : ngày sinh tăng dần: (nhỏ hơn)
    def __lt__(self, other):
        # if self.date_of_birth['nam'] == other.date_of_birth['nam']:
        #     if self.date_of_birth['thang'] == other.date_of_birth['thang']:
        #         return self.date_of_birth['ngay'] < other.date_of_birth['ngay']
        #     else:
        #         return self.date_of_birth['thang'] < other.date_of_birth['thang']
        #
        # return self.date_of_birth['nam'] < other.date_of_birth['nam']
        date_self = datetime(self.date_of_birth['nam'], self.date_of_birth['thang'], self.date_of_birth['ngay'])
        date_other = datetime(other.date_of_birth['nam'], other.date_of_birth['thang'], other.date_of_birth['ngay'])

        return date_self < date_other

### Nhập vào một danh sách sinh viên
students = []
while True:
    id = input("Id: ")
    name = input("Name: ")
    score1 = float(input("Diem mon 1: "))
    score2 = float(input("Diem mon 2: "))

    # Nhap ngay thang nam
    ngay, thang, nam = map(int, input("Nhap ngay thang nam sinh (ngay/thang/nam): ").split("/"))

    date_of_birth = {
        'ngay': ngay,
        'thang': thang,
        'nam': nam
    }

    # Tạo đối tượng sinh viên
    students.append(Student(id, name, score1, score2, date_of_birth))

    if input("Ban co muon tiep tuc (y/n): ") == "n":
        break

## In ra sinh viên, sắp xếp ngày tăng dần
students.sort()
print("=" * 20, " IN THONG TIN")
for student in students:
    print(student)
