import utils
# Tinh tích 2 ma trận a, b

"""
    a[i][j] (tính theo hàng) j chạy * b[i][j] (tính theo cột) i chạy
"""

# Nhap hang, cot
hang_a = int(input("Nhap so hang ma tran A"))
cot_a = int(input("Nhap so cot ma tran A"))
hang_b = cot_a
cot_b = int(input("Nhap so cot ma tran B"))


a = []
b = []
c = []

# Nhap ma tran a
for i in range(hang_a):
    row = []
    for j in range(cot_a):
        row.append(int(input(f"Nhap a[{i}][{j}]: ")))
    a.append(row)

# Nhap ma tran b
for i in range(hang_b):
    row = []
    for j in range(cot_b):
        row.append(int(input(f"b[{i}][{j}] = ")))
    b.append(row)

utils.in_ma_tran(a)
utils.in_ma_tran(b)

# Tinh tich 2 ma tran: (hang_a, cot_b)
c = [[0 for _ in range(cot_b)] for _ in range(hang_a)]

for i in range(hang_a):
    for j in range(cot_b):
        # Tinh c[i][j] = [](hang_a x cot_b)
        for k in range(cot_a):
            c[i][j] += a[i][k]*b[k][j]

print("Ma tran tich c:")
utils.in_ma_tran(c)

