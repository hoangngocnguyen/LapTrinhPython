# ...ép kiểu

########## toán tử ################
# soNgay = int(input("Nhập vào số ngày: "))
# soTuan = soNgay // 7
# soNgayLe = soNgay % 7
#
# print(f'Khách đã ở {soTuan} tuần và {soNgayLe} ngày lẻ')

############### Toán tử gán ###########
# i = 1
# while i < 10:
#     print(i)
#     i += 1


#############   Buổi 2 ####################

### 1. Nhập dữ liệu:
# namSinh = input("Năm sinh: ")
# print(type(namSinh))
#
# tuoi = 2025 - int(namSinh)
# print("Tuoi cua ban la:", tuoi)

# namSinh = int(input("Năm sinh: "))
# print(type(namSinh))
#
# tuoi = 2025 - namSinh
# print("Tuoi cua ban la:", tuoi)

### 2. Nhập bán kính r, tính diện tích
# r = float(input("Nhập bán kính r: "))
# s = 3.14*r*r
# c = 2*r*3.14
# print(f'Diện tích hình tròn là {s}')
# print(f'Chu vi hình tròn là {c}')

#### 3. Nhập 4 số nguyên trên 1 dòng

## C1. Làm từ từ. Tách rồi ánh xạ sang các phần tử
# st = input("Nhap 4 so nguyen")
# st = st.split()         # List các phần tử kiểu string
# print(st)
#
# # Ánh xạ từng phần tử của st sang a, b, c, d và kiểu int. 2 bên phải tương đương số phần tử.
# a, b, c, d = map(int, st)
# print(a+b+c+d)

## C2. Làm gộp
# a, b, c, d = map(int, input("Nhập 4 số nguyên trên 1 dòng:").split())
# print(a+b+c+d)


################# if #########
# dtb = float(input("DTB: "))
# if dtb > 7:
#     print("Dau")
#     print(f"Chuc mung ban dau voi so diem: {dtb}")
# else:
#     print(f"Chuc ban thi lai vui ve! Ban chi duoc {dtb} diem")
#
# if 0 <= dtb <= 10:
#     print("Diem trung binh hop le")
# else:
#     print("Diem trung binh khong hop le")


## 1. Kiểm tra số chẵn chia hết cho 3
# number = int(input("Nhap so nguyen: "))
# if (number % 2 == 0) and (number % 3 == 0):
#     print("Yes")
# else:
#     print("No")


#################### if elif ###################
'''
Từ 3.6 - 4: xx
3.2 gioi
2.5 kha
2 tb
1 yeu
kem
'''

# dtb = float(input("Nhập vào DTB: "))
# if dtb > 4.0 or dtb < 0:
#     print("Diem khong hop le")
# elif dtb >= 3.6:
#     print("Xuat sac")
# elif dtb >= 3.2:
#     print("Gioi")
# elif dtb >= 2.5:
#     print("Kha")
# elif dtb >= 2:
#     print("Trung binh")
# elif dtb >= 1:
#     print("Yeu")
# else:
#     print("Kem")


############### VÒNG LẶP FOR ####################
# for i in range(10):
#     print(i, end=" ")
#
# print()
# for i in range(2, 10, 2):
#     print(i, end=" ")
#
#
# print()
# for i in range(20, 10, -2):
#     print(i, end=" ")


###. Bài tập: Tính tổng S = 1 + 2 + ... n với n là số nguyên nhập từ bàn phím
# n = int(input("Nhập số nguyên n: "))
# S = 0
# for i in range(1, n+1):
#     S += i
# print(S)
#
# S = int((n + 1)*n/2)
# print(S)


### Bài tập: tính giai thừa của n
# n = int(input("Nhập n: "))
# S = 1
# for i in range(1, n + 1):
#     S *= i
# print(f"Giai thừa của {n} là: {S}")
#
#
# ## Dùng đệ quy
# def giai_thua(n):
#     if n == 0:
#         return 1
#     else:
#         return n * giai_thua(n - 1)
#
#
# print(giai_thua(n))


### Bài tập: Kiểm tra số nhập vào là Số hoàn hảo, số có tổng các ước thực sự bằng chính nó (ước thực sự là ước, trừ chính nó)
import math

n = int(input("Nhập n: "))
S = 0
for i in range(1, int(n/2 + 1)):
    if n % i == 0:
        S += i

if S == n:
    print(f"Số {n} là số hoàn hảo")
else:
    print(f"Số {n} không phải là số hoàn hảo")

