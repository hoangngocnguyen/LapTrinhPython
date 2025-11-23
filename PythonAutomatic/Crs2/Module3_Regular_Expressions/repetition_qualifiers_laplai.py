import re
# Lặp lại điều kiện

### 1. Dấu * (Zero or More) Phần tử trước đó lặp 0 lần hoặc nhiều lần
# Dấu chấm là bất kỳ, * là nhiều ký tự bất kỳ sau đó.
print(re.search(r"Py.*thon", "Pyyyyyython"))

# Lặp lại vùng [a-z] nhiều lần sau đó -> Python.
print(re.search(r"Py[a-z]*n", "Python Programming"))

# Ra null, vì không có khớp. Vì sau Pyth là dấu cách rồi, không thể có n ở cuối
print(re.search(r"Py[a-z]*n", "Pyth on Programming"))


### 2. Dấu + (One or More) Phần tử trước đó lặp 1 lần hoặc nhiều lần
# Ra ol luôn
print(re.search(r"o+l+", "goldfish"))

# Ra ooll
print(re.search(r"o+l+", "woolly"))

# ra None vì giữa ol là i.
print(re.search(r"o+l+", "boil"))


### 3. ? Có thể có hoặc không
print(re.search(r"I?love you", "love you"))
print(re.search(r"I?like peac", "I like peaches"))


### Phân biệt nhẹ * và +

# *: có hoặc không có a vẫn khớp
print(re.search(r"ILovea*s", "ILoveaaas"))
print(re.search(r"ILovea*s", "ILoves"))

# +: phải có ít nhất 1.
# None vì không có a
print(re.search(r"ILovea+s", "ILoves"))
print(re.search(r"ILovea+s", "ILoveas"))
print(re.search(r"ILovea+s", "ILoveaaas"))