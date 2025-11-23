# List lồng list
lst = [
    [12455,2,3],
    [4,5111,6],
    [7,8,999]
]

print(lst[2][1])
print(lst)

# in ma tran dep
print("In ma tran dep")
for row in lst:
    print(row)

# in ma tran dep 2
for row in lst:
    for e in row:
        print(f"{e:<12}", end="")
    print()

for row in lst:
    for e in row:
        print(f"{e:>12}", end="")
    print()


for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(f"{lst[i][j]:<12}", end=" ")
    print()


# Ma tran cac phan tu = 0
m = 3
n = 4
a = [[0 for _ in range(n)] for _ in range(m)]

# m = 0 , n = 1,2,3,4
# m = 1, n = 1,2,3,4
# m = 2, n = 1,2,3,4

print(a)


# Nhap vao
a = []
m = int(input("So dong: "))
n = int(input("So cot: "))

for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"a[{i}][{j}]")))
    a.append(row)

print(a)
for row in a:
    for e in row:
        print(f"{e:<10}", end="")
    print()

# Nhap ma tran a, b tính tong hai ma tran

