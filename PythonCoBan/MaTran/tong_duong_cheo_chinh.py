import utils

hang = int(input("Nhap so hang: "))
cot = int(input("Nhap so cot: "))
a= utils.nhap_ma_tran(hang, cot)


utils.in_ma_tran(a)
print(f"Tong cac phan tu tren duong cheo chinh: {utils.tong_duong_cheo_chinh(a, hang, cot)}")
