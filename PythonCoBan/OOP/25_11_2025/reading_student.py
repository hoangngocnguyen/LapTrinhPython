from datetime import datetime

def format_date(date):
    return f"{date['ngay']}/{date['thang']}/{date['nam']}"
class Student:
    subject = "Python"

    def __init__(self, id_student, name, score1, score2, score3, date_of_birth):
        self.id = id_student
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.date_of_birth = date_of_birth

    def score(self):
        return round((self.score1 + self.score2 + self.score3) / 3)

    def __str__(self):
        return f"{self.name:<20} {format_date(self.date_of_birth):<15} {self.score():<10}"

    # Qúa tải cho < : ngày sinh tăng dần: (nhỏ hơn)
    def __lt__(self, other):
        # if self.date_of_birth['nam'] == other.date_of_birth['nam']:
        #     if self.date_of_birth['thang'] == other.date_of_birth['thang']:
        #         return self.date_of_birth['ngay'] < other.date_of_birth['ngay']
        #     else:
        #         return self.date_of_birth['thang'] < other.date_of_birth['thang']
        #
        # return self.date_of_birth['nam'] < other.date_of_birth['nam']

        # Ép kiểu về date object
        date_self = datetime(self.date_of_birth['nam'], self.date_of_birth['thang'], self.date_of_birth['ngay'])
        date_other = datetime(other.date_of_birth['nam'], other.date_of_birth['thang'], other.date_of_birth['ngay'])

        return date_self < date_other


### Đọc sinh viên và in ra từ file student.txt
students = []
file = open("student.txt")

# Ánh xạ dữ liệu vào mảng
lines = file.readlines()

for line in lines:
    line = line.strip().split(";")

    line = [x.strip() for x in line]

    id, name = line[0:2]
    sc1, sc2, sc3 = map(float, line[2:5])

    # Nhap ngay thang nam
    ngay, thang, nam = map(int, line[5].split("/"))

    date_of_birth = {
        'ngay': ngay,
        'thang': thang,
        'nam': nam
    }

    students.append(Student(id, name, sc1, sc2, sc3, date_of_birth))


## In ra sinh viên
print("="*20, " IN THONG TIN")
print(f"{'Ten':<20} {'Ngay sinh':<15} {'DTB':<10}")
students.sort()
for student in students:
   print(student)


file.close()
