#1 đối tượng không thể thay đổi thuộc tính của lớp
# 1  đối tượng thay đổi thuộc tính của lớp -> tạo một thuộc tính mới, thành thuộc tính của riêng nó

"""
    subject = Python
    a.subject = Java
    in a.subject ---> Java
    in b.subject ---> Vẫn Python
"""

class Student:
    subject = "Python"

    #Phương thức khởi tạo

    # Hàm init tự động chạy khi gọi lớp và truyền thamm số
    # Gán các thuộc tính với các giá trị truyền vào
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score
    def get_info(self):
        print(f"id: {self.id}, name: {self.name}, score: {self.score}")


sv1 = Student("1", "Hoàng", 9)  # self là sv1
sv2 = Student("2", "Cindy", 3)
sv3 = Student("3", "Linda", 6)


sv1.subject = "Java"

print(sv1.subject)
print(sv2.subject)

print(Student.subject)
Student.subject = "Javascript"

print(sv2.subject)

sv2.get_info()