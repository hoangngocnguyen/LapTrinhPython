import csv

products = [["Iphone 15", "40 M"],["Samsung J1", "2 M"]]

# Mở file ra để ghi, newline giải quyết vấn đề ngắt dòng khi ghi file.
# (ngắt của window, ngắt của csv là 2, dẫn đến hàng sau null)
with open ("products.csv", "w", newline="") as products_csv:
    # Tạo đối tượng ghi
    #Đối tượng writer này sẽ chịu trách nhiệm định dạng và ghi dữ liệu theo tiêu chuẩn CSV.
    writer = csv.writer(products_csv)

    # Ghi dữ liệu theo hàng - (List of Lists)
    writer.writerows(products)


# Bài 2:
n = int(input("Nhap n"))

list = []

for i in range(n):
    maSV = input("Ma sinh vien:")
    hoTen = input("Ho ten:")
    sdt = input("Sdt: ")

    # Luu thong tin
    sinhvien = {}
    sinhvien.update(
        {
            'maSV': maSV,
            'hoTen': hoTen,
            'sdt': sdt
        }
    )
    print(sinhvien)

    list.append(sinhvien)

print(list)

ma = input("Nhap ma sinh vien")
for sv in list:
    if sv["maSV"] == ma:
        print(sv)

