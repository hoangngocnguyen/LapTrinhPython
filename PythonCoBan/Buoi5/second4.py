"""
    SET trong Python
"""

# s = {1, 1}
# print(s)
# # print(s[0])
#
# a = [1, 1]
# print(a)


"""
    add, update set
"""

# s = {1, 2, 3, 4}
# # s.add(1, 2)
# s.add(8)                # Chỉ thêm được 1 giá trị.
# print(s)
#
#
# s.update({10, 11, 1, 2})      # Thêm 10 và 11, dùng {} như []. Thêm những phần khác.
# print(s)
#
# s.update([2005, 2000])  # Thêm 2005, 2000 như trên
# print(s)

"""
    set remove and discard
"""

# s = {1, 2, 3}
# s.remove(3)
# print(s)
#
# s.remove(3)     # Báo lỗi nếu phần tử cần xóa không tồn tại
# print(s)
#
#
# s.discard(3)
# s.discard(3)      # Không báo lỗi
# print(s)

"""
    set union (hợp), set intersection (giao), set difference (hiệu), set symmetric_difference (không chung)
"""

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(f"set 1: {s1}")
print(f"set 2: {s2}")

union = s1.union(s2)
print(f"Hợp của s1 và s2: {union}")

intersection = s1.intersection(s2)
print(f"Giao của s1 và s2: {intersection}")

diff = s1.difference(s2)
print(f"s1 hiệu s2: {diff}")

symDiff = s1.symmetric_difference(s2)
print(f"Các phần tử không chung giữa s1 và s2: {symDiff}")



