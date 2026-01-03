### 1a> Nhap diem 3 mon -> in ra dtb va xep loai
toan = float(input("Diem toan: "))
van = float(input("Diem van: "))
anh = float(input("Diem anh: "))

dtb = (toan + van + anh) / 3

xloai = ""
if dtb >= 8.0:
    xloai = "Giỏi"
elif dtb >= 6.5:
    xloai = "Khá"
elif dtb >= 5.0:
    xloai = "Trung binh"
else:
    xloai = "Yếu"

print(f"DTB: {dtb:.2f}, Xep loai: {xloai}")


