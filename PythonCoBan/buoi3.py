"""
    Vòng lặp while
"""

# print('Đếm số chữ số của một số nguyên')
#
# n = 12345
# cnt = 0
# while n > 0:
#     cnt += 1
#     n = n // 10
# print(f'So chu so cua n la: {cnt}')
#
# n = 12345
# print(f'So chu so cua n la: {len(str(n))}')

#################################################
# print('Tính tổng các chữ số của một số nguyên')
# n = 12345
# s = 0
# while n > 0:
#     sodu = n % 10
#     s += sodu
#     n = n // 10
# print(f'Tong cac chu so cua n = {n} la: {s}')


#################################################
# print('Tính tổng các chữ số của một số nguyên')
# n = 1234555
# s = 0
# while n > 0:
#     sodu = n % 10
#     if sodu % 2 == 1:
#         s += sodu
#     n = n // 10
# print(f'Tong cac chu so le cua n = {n} la: {s}')


# Nhâp số nguyên từ bàn phím cho đến khi n thuộc [0, 10]
# n = None
# while True:
#     n = int(input("Nhap n:"))
#     if 0 <= n <= 10:
#         break
#     print("Du lieu chua hop le. Vui long nhap lai")
#
# print(f'So vua nhap la {n}')


# Nhập số nguyên n. Tính S = 1/2 + 2/3 + 3/4 + .. n/n+1
# n = int(input("Nhap n:"))
# s = 0
# for i in range(1, n + 1):
#     s += i / (i + 1)
#
# print(f"S = {round(s, 2)}")


# Kiểm tra n nhập vào có phải là số nguyên tố
n = int(input("nhap n: "))


def isSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True


print(f"{n} la so nguyen to? {isSoNguyenTo(n)}")
