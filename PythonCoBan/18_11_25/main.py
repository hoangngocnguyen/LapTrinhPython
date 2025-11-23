# Bài 2:
n = int(input("Nhap n"))

list = []

for i in range(n):
    sv = {}
    # maSV = input("Ma sinh vien:")
    # hoTen = input("Ho ten:")
    # sdt = input("Sdt: ")
    #
    # # Luu thong tin
    # sinhvien = {}
    # sinhvien.update(
    #     {
    #         'maSV': maSV,
    #         'hoTen': hoTen,
    #         'sdt': sdt
    #     }
    # )

    sv['maSV'] = input("Ma sinh vien:")
    sv['hoTen'] = input("Ho ten:")
    sv['sdt'] = input("Sdt: ")
    list.append(sv)

print(list)

ma = input("Nhap ma sinh vien")
print("Hiển thị:")

co = False
for sv in list:
    if sv["maSV"] == ma:
        co = True
        print(sv)

if not co:
    print("Không tim thay")

