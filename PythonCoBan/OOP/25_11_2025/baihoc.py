class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_info(self):
        return f"Sản phẩm: {self.name}, Giá: {self.price}, Số lượng: {self.quantity}"


class Person:
    def __int__(self, id):
        self.id = id

    def get_info(self):
        return f"Nguoi nay co id la {self.id}"


class Student:
    subject = "Python"

    def __init__(self, id_student, name, score1, score2, score3):
        self.id = id_student
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def avg_score(self):
        return round((self.score1 + 2 * self.score2 + 3 * self.score3) / 6, 2)

    def get_info(self):
        return f"Ma: {self.name}; Ten: {self.name}; Diem1: {self.score1}; Diem2: {self.score2}; Diem3: {self.score3}; DTB: {self.avg_score():.2f}"

    # Qúa tải cho < (less than), tự chạy khi dùng hàm .sort()
    def __lt__(self, other):
        return self.avg_score() < other.avg_score()

    def __str__(self):
        return f"{self.name}; {self.avg_score()}"

st1 = Student("1", "Hoang", 4, 5, 6)
print(st1.avg_score())
print(st1.get_info())


### Nhập vào một danh sách sinh viên
students = []
while True:
    id = input("Id: ")
    name = input("Name: ")
    score1 = float(input("Diem mon 1: "))
    score2 = float(input("Diem mon 2: "))
    score3 = float(input("Diem mon 3: "))

    # Tạo đối tượng sinh viên
    students.append(Student(id, name, score1, score2, score3))

    if input("Ban co muon tiep tuc (y/n): ") == "n":
        break


## In ra sinh viên
print("="*20, " IN THONG TIN")
for student in students:
    print(student.get_info())


## Sắp xếp sinh viên theo điểm trung binh
print("="*20, " SẮP XẾP THEO ĐTB")
for student in sorted(students, key=lambda s: s.avg_score(), reverse=True):
    print(student.get_info())






