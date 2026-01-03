### Xay dung class
class BankAccount:
    def __init__(self, soTK, chuTK, soDu: int):
        self.soTK = soTK
        self.chuTK = chuTK
        self.soDu = soDu

    ## Method them tien vao tk
    def them_tien(self, money):
        self.soDu += money

    ## Rut tien
    def rut_tien(self, money):
        ## So tien rut duoc
        tien_co_the_rut = self.soDu - 50000
        if money <= tien_co_the_rut:
            self.soDu -= money
        else:
            print(f"So tien trong tai khoan khong du. So du hien co: {self.soDu}")

    ## In thong tin
    def in_thong_tin(self):
        print(f"[STK]: {self.soTK}; [CHU TK]: {self.chuTK}; [SO DU]: {self.soDu}")

    def getSoDu(self):
        return self.soDu

### b.

""" Nhap so tai khoan va so tien can rut
    STK khong ton tai -> Khong ton tai so tai khoan nay
"""
lst_account = []
# Doc du lieu
with open("ThongtinTK.txt", encoding="utf-8") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    for line in lines:
        line = line.split(',')
        soTK, chuTK = line[0], line[1]
        soDu = int(line[2])

        acc = BankAccount(soTK, chuTK, soDu)
        lst_account.append(acc)



def tim_tai_khoan(stk: str):
    for tk in lst_account:
        tk: BankAccount
        if tk.soTK == stk:
            return tk

    return None

stk = input("Nhap stk can rut: ")
tien_rut = int(input("Nhap so tien can rut: "))
acc = tim_tai_khoan(stk)

if acc:
    acc.rut_tien(tien_rut)
else:
    print("Khong ton tai so tai khoan nay")


print("\nDanh sach tang dan so du")
lst_account.sort(key=lambda acc: acc.getSoDu())

for acc in lst_account:
    acc.in_thong_tin()