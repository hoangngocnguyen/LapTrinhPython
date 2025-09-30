def tong(x, y):
    return x + y


def in_ket_qua(ho_ten, diem):
    print("Ho ten: ", ho_ten)
    print("Diem: ", diem)


def ket_qua(ho_ten, diem_toan, diem_tin):
    tong = diem_tin + diem_toan
    return ho_ten, tong


def hoan(a, b):
    return b, a


def info(name, sub="Đẹp trai"):
    print(f"Xin chào {name} {sub}")


def giai_thua(n):
    if n == 0:
        return 1
    return n * giai_thua(n - 1)


def C_n_k(n, k):
    return int(giai_thua(n) / (giai_thua(k) * giai_thua(n - k)))


def is_so_hoan_hao(n):
    S = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            S += i

    if S == n:
        return True
    else:
        return False



if __name__ == "__main__":
    # Code chỉ chạy ở đây, không ảnh hưởng đến các file khác
    # print(f'tong cua {1} và {4} là: {tong(1,4)}')

    # in_ket_qua("Nam", 9)
    # in_ket_qua(9, "Nam")
    # in_ket_qua(diem=9, ho_ten="Nam")

    # print(type(ket_qua("Hoang", 10, 10)))

    # a = 1
    # b = 2
    # a, b = hoan(a, b)
    # print(a, b)

    # info("Đạt", "Áo đen")
    # info("Hoang")

    # print(giai_thua(5))

    # print(C_n_k(7, 2))

    # n = int(input("Nhập n: "))
    # print(f"Mệnh đề {n} la sô hoàn hào là: {is_so_hoan_hao(n)}")

    print()
