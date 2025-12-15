from datetime import datetime
import csv

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
    # Sử dụng class datetime
    # def __lt__(self, other):
    #     # Ép dictionary date_of_birth sang obj datetime
    #     date_self = datetime(self.date_of_birth['nam'], self.date_of_birth['thang'], self.date_of_birth['ngay'])
    #     date_other = datetime(other.date_of_birth['nam'], other.date_of_birth['thang'], other.date_of_birth['ngay'])
    #     return date_self < date_other


    def __gt__(self, other):
        # Ép dictionary date_of_birth sang obj datetime
        date_self = datetime(self.date_of_birth['nam'], self.date_of_birth['thang'], self.date_of_birth['ngay'])
        date_other = datetime(other.date_of_birth['nam'], other.date_of_birth['thang'], other.date_of_birth['ngay'])
        return date_self > date_other

### Đọc sinh viên và in ra từ file student.txt
students = []

# Ánh xạ dữ liệu vào mảng
with open("student.txt", encoding="utf-8") as file:
    lines = csv.reader(file, delimiter=';')

    for line in lines:
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
print("="*20, " IN THONG TIN - Trước sắp xếp")
print(f"{'Ten':<20} {'Ngay sinh':<15} {'DTB':<10}")
for student in students:
   print(student)

print("="*20, " IN THONG TIN - Sau sắp xếp")
print(f"{'Ten':<20} {'Ngay sinh':<15} {'DTB':<10}")
# students.sort()

# students.sort(key= lambda sv: (datetime(sv.date_of_birth['nam'], sv.date_of_birth['thang'], sv.date_of_birth['ngay']), sv.score()))

# Sắp xếp điểm trung bình cao lên trên (giảm dần) | -a, -b
students.sort(key= lambda sv: (datetime(sv.date_of_birth['nam'], sv.date_of_birth['thang'], sv.date_of_birth['ngay']), -sv.score()))
# students.sort(key= lambda sv: sv.score())
for student in students:
   print(student)



"""
Nếu đề bắt dùng __gt__ để sẵp thì sao???
+ hàm sort có mặc định là lt
+ Dùng students.sort(reverse=True)
+ gt đảo tham số -> giống như lt (a<b)

Python cần: Xác định A < B đúng hay sai: nếu đúng (a trước b, giu nguyen)
"""


