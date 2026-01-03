"""
a. Tao ds ng dung
kthuc: TenDangNhap rong
- Kiem tra ten dang nhap trung -> nhap lai
"""

lst_user = []
lst_tendn = []
while True:
    TenDangNhap = input("Nhap TenDangNhap: ")
    if TenDangNhap == "":
        break
    if TenDangNhap in lst_tendn:
        print("Ten dang nhap da ton tai. Vui long nhap lai.")
        continue

    lst_tendn.append(TenDangNhap)

    MatKhau = input("Nhap MatKhau: ")
    HoTen = input("Nhap HoTen: ")
    NamSinh = int(input("Nhap NamSinh: "))
    SDT = input("Nhap SDT: ")

    lst_user.append({
        "TenDangNhap" : TenDangNhap,
        "MatKhau" : MatKhau,
        "HoTen" : HoTen,
        "NamSinh" : NamSinh,
        "SDT" : SDT,
    })


"""
b. In ra nguoi dung nho hon 30 tuoi.
    In ra nguoi dung co ten "Nam" khong pb hoa thuong
"""

def display(user):
    print(f"{user['TenDangNhap']:<10}{user['MatKhau'] : <10}{user['HoTen'] : <20}"
          f"{user['NamSinh'] :<8}{user['SDT'] :<14}")


## Nho hon 30 tuoi
from datetime import datetime
print("\nDanh sach tuoi hon 30")
for user in lst_user:
    ## Lay tuoi
    this_year = datetime.now().year
    age = this_year - user['NamSinh']

    if age > 30:
        display(user)


print("Danh sach ten Nam")
for user in lst_user:
    ## Lay ten
    hoten: str = user['HoTen']
    ten: str = hoten.split()[-1]

    if ten.lower() == "nam".lower():
        display(user)

"""
c. In ngdung matkhau yeu:
Khong yeu ~ len >8 , 1 chu so, 1 chu cai, 1 ky tu khac chu so chu cai 
"""
def is_strong_password(password: str):
    ## len
    size = len(password)

    ## So chu so
    num_cnt = 0
    alpha_cnt = 0
    other_cnt = 0
    for c in password:
        if c.isdecimal():
            num_cnt += 1
        if c.isalpha():
            alpha_cnt += 1
        if not c.isalnum():
            other_cnt += 1

    return size > 8 and num_cnt > 0 and alpha_cnt > 0 and other_cnt > 0
print("\nDanh sach mat khau yeu")
for user in lst_user:
    if not is_strong_password(user['MatKhau']):
        display(user)

