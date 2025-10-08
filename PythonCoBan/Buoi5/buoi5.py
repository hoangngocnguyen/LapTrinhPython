"""
    LIST
"""

so = [1,2,3,4,5,6,7,8]

so_chan = [n for n in so if n%2==0]
print(so_chan)


# Tạo List rỗng
lst = [1, "handsome", 2.4]
print([print(type(item), item) for item in lst])  # Phải dùng trong ngoặc vuông[...]


# Ép kiểu sang list

a = list(range(10))
print(a)
print(''.rjust(30, '-'))

st = "Love Cindy"
L = list(st)
print(L)
print(''.rjust(30, '-'))

# Hàm len()
print(f"So luong phan tu: {len(L)}")
print(''.rjust(30, '-'))

# Truy cập phần tử
print(L[-2], L[8])
print(''.rjust(30, '-'))


# Lấy nhiều phần tử
print(L[0:4])
print(''.rjust(30, '-'))


### Duyệt list
so_le = [n for n in so if n%2==1]
print(so_le)

for i in range(len(so_le)):
    print(so_le[i])

for number in so_le:
    print(number)

print(''.rjust(30, '-'))
print("Thêm phần tử vào cuối list: apppend()")

print(so_le)
so_le.append(9)

print(so_le)


print(''.rjust(30, '-'))
print("Insert")
so_le.insert(2, "insert")

so_le.insert(len(so_le), "chencuoi")

so_le.insert(0, "chendau")
print(so_le)


print(''.rjust(30, '-'))
print("Xóa phần tử theo chỉ số: pop()")

so_le.pop()     # mặc định xóa cuối
print(so_le)

so_le.pop(0)
print(so_le)

##################
print(''.rjust(30, '-'))
print("Xóa phần tử theo giá trị: remove()")

so_le = [1, 2, 3, 4, 5, 5, 2, 1]

print(so_le)
so_le.remove(1)
print(so_le)

so_le.remove(4)
print(so_le)

so_le.append(1)
so_le.append(1)

print(so_le)

so_le = [x for x in so_le if x != 1]
print(so_le)

so_le.clear()
print(so_le)

##########
print(''.rjust(30, '-'))

n = 9
a = [0] * 9
print(a)


print(''.rjust(30, '-'))
a = [1, 2, 3, 4, 5, 6, 7, "tam", 9.0, 10/1, 2/1]

if 10 in a:
    print("Yes")
else:
    print("No")

print(a.count(2))

print(a.index(2), ",", a.index("tam"))

print(''.rjust(30, '-'))
print(a)
a.reverse()
print(a)


print(''.rjust(30, '-'))
a = [1, 2, 3, 4, 5, 6, 7]
a.sort(reverse=True)



















