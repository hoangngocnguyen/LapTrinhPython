import utils

hang = int(input("Nhap so hang: "))
cot = int(input("Nhap so cot: "))

a = [[0 for _ in range(cot)] for _ in range(hang)]
for i in range(hang):
    for j in range(cot):
        a[i][j] = int(input(f"a[{i}][{j}]= "))

utils.in_ma_tran(a)

if utils.is_doi_xung(a, hang, cot):
    print("Đối xứng")
else:
    print("Không đối xứng")