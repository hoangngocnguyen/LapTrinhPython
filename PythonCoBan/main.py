# key = 99
# for i in [1, 2, 3, 4, 5]:
#     if i == key:
#         print(f"Có {key}")
#         break
# else:
#     print(f"Không có số {key} trong danh sách")
#
# print(say := "hello")
# print(say)
#
# if (n := len("Hoang dep trai")) > 5:
#     print(f"Length is greater than 5: {n}")
#
# hi = lambda: print("Hillo")
# hi()
#

######################## List ###########
### 1. Slice
furniture = ['table', 'chair', 'tivi', 'bed', 'led']

# slice_1 = furniture[0:3]
#
# for item in slice_1:
#     print(item)

### 2. copy all list, append()
# slice_copy = furniture[:]
#
# slice_copy.append("hoang")
# for item in slice_copy:
#     print(item)
#
# print("Length of list", len(slice_copy))

### 3. Change values with indexs
# furniture[0] = "Deptrai"
# furniture[-2] = "Haha"
# print(furniture)


### 4. Concatenation (nối) and Replication (nhân)
# a = [1, 2, 3]
# b = a*3
# print(b)
# c = b + ['a', 'b', 'c']
# print(c)

### 5. Getting the "index" in a loop with enumerate()
# phones = ['apple', 'samsung', 'oppo', 'xiaomi']
# for item in phones:
#     print(item)
# for index, item in enumerate(phones):
#     print(f"index: {index} - item: {item}")


### 6. Loop in Multiple Lists with zip()
# phones = ['apple', 'samsung', 'oppo', 'xiaomi']
# ratings = [4.8, 4.6, 4.5, 4.9]
#
# for phone, rating in zip(phones, ratings):
#     print(f"The phone: {phone} has {rating} star")

### 7. The in and not in operators
# phones = ['apple', 'samsung', 'oppo', 'xiaomi']
# key = 'honor'
# if key in phones:
#     print(f"Key: {key} co xuat hien trong {phones}")
# else:
#     print(f"Key: {key} khong xuat hien trong {phones}")



### 8. The Multiple Assignment Trick: gán cho nhiều biến một lúc
# phones = ['apple', 'samsung', 'oppo', 'xiaomi']
# apple, samsung, oppo, xiaomi = phones
#
# print(apple, samsung, oppo, xiaomi)
#
# # có thể dùng để swap 2 biến
# apple, samsung = samsung, apple
# print(apple, samsung)



#### 9. The index Method. Lấy ra vị trí của phần tử có giá trị trong list
# phones = ['apple', 'samsung', 'oppo', 'xiaomi']
# print(phones.index('samsung'))


### 10. Adding values
# append(): adds an element to the end of the list
# insert(): adds an element to a list at a given position
# phones = ['apple', 'samsung', 'oppo', 'xiaomi']
# phones.append('tecno')
# print(phones)
#
# phones.insert(1, 'googlePixel')
# print(phones)

### 11. Removing Values
'''
+ del(): xóa phần tử theo index
+ remove(): xóa phần tử theo giá trị. Chỉ xóa phần tử khớp đầu tiên.
+ pop(): mặc định - xóa phần tử cuối và trả về nó. Có thể dùng index để chỉ định.
'''
phones = ['apple', 'samsung', 'oppo', 'xiaomi']


del(phones[2])  #tương tự: del phones[2]
print(phones)

phones = ['apple', 'samsung', 'oppo', 'xiaomi']
phones.remove("oppo")
print(phones)

phones = ['apple', 'samsung', 'oppo', 'xiaomi']
phones.remove("oppo")
print(phones)