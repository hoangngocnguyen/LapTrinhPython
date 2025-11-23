
# for i in range(m):
#     row = []
#     for j in range(n):
#         row.append(int(input(f"a[{i}][{j}]")))
#     a.append(row)

a = [
    [1, 2, 3],
    [4, 5, 6],
    [2, 2, 2],
]
b = [
    [1, 0, 0],
    [12, 1, 0],
    [2, 2, 1],
]

# TInh tong 2 ma tran
c = []
# for i in range(len(a)):
#     # Tong hang
#     row = []
#     for j in range(len(a)):
#         print(f"a[{i}][{j}]= ", a[i][j])
#         print(f"b[{i}][{j}]= ", b[i][j])
#         value = a[i][j] + b[i][j]
#         row.append(value)
#     c.append(row)

### Nếu row_a, row_b in a, b: thì Python hiểu đang giải a cho row_a, row_b
# for row_a, row_b in zip(a, b):
#     # Tong hang
#     row = []
#     for a, b in zip(row_a, row_b):
#         value = a + b
#         row.append(value)
#     c.append(row)

c = [[0 for _ in range(len(a))] for _ in range(len(a))]
for i in range(len(a)):
    # Duyet tung hang
    for j in range(len(a[i])):
        c[i][j] = a[i][j] + b[i][j]

for row in c:
    for e in row:
        print(f"{e:<10}", end="")
    print()



