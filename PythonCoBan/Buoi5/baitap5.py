# Nhập mảng số nguyên -> tính tổng
# list = list(map(int, input("Nhập mảng số nguyên:").split()))
# s = 0
# for i in list:
#     s += i
# print(s)
#
# print(sum(list))

### bai tap 2
# list = list(map(int, input("Nhập mảng số nguyên:").split()))
# x = int(input("nhap x: "))

## 2 for
# if x not in list:
#     print(-1)
#
# for i in range(len(list)):
#     if x == list[i]:
#         print(i, end= " ")

# co = False
# for i in range(len(list)):
#     if x == list[i]:
#         print(i, end= " ")
#         co = True
# if co == False:
#     print(-1)



def isTang(lst):
    for i in range(len(lst) - 1):
        if lst[i+1] < lst[i]:
            return False
    return True

list = list(map(int, input("Nhập mảng số nguyên:").split()))


print(isTang(list))

