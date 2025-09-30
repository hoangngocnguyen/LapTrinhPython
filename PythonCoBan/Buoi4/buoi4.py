'''
    Hàm
'''


# a, b, c = map(int, input("Nhập 3 số liên tục").split())
# print(a, b, c)
# nhập chuỗi (input), tách chuỗi -> thành mảng (split), ánh xạ mảng kí tự sang số nguyên (map)

def xin_chao():
    print("Xin chao ban!")

# xin_chao()

# def tong(a, b):
#     return a + b
#
#
# a = 1
# b = 2
# c = tong(a, b)
# print(f'Tong cua {a} và {b} la: {c}')


'''
    __name__ = __main__: 
        + sử dụng ở các file (thường là file xây dựng hàm tiện ích)
        + chỉ định code chỉ được chạy trực tiếp trong file chứa code đó (code test hàm,...)
        + khi file khác cần import file này thì code không bị lây lan.
'''

import CacHam

# Đây là file hiện tại.
print(CacHam.tong(1, 2))




