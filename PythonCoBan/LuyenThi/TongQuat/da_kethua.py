class Bird:
    def move(self):
        print("Đang bay...")

class Fish:
    def move(self):
        print("Đang bơi...")

# Ke thua ca 2
class Duck(Bird, Fish):
    pass        ## Để cho có chỗ, đỡ bị lỗi chương trình

vịt = Duck()
vịt.move()