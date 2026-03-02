# Tuple bất biến, chỉ khởi tạo 1 lần, ko add, ko update
a = (1,2,3,3,5)

print(a)
print(type(a))

lst = list(a)
lst.append("thêm")
print(lst)

b = (1, "Hoàng")
id, name = b
print(id, name)