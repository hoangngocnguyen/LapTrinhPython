# https://coder.husc.edu.vn/problem/drone2
import math

def solve():
    a, b, k = map(int, input().split())


    if k == 1:
        diem_tren = a + b + math.gcd(a, b)

        print(diem_tren)
    elif k == 2:
        diem_tren = a + b + math.gcd(a, b)
        diem_trong = (a*b - diem_tren + 2)//2

        print(diem_trong)

if __name__ == "__main__":
    solve()