import re

# st = input()
st = "5 random strings contain .three numbers: 32, 3.14, 24, 32.15, 2.0 .13"
# Regex này nếu đảo ngược sẽ ưu tiên tìm số nguyên đầu tiên (dẫn đến chỉ tìm so nguyên)
pattern = r"[-]?\d+\.\d+|[-]?\d+"
match = re.findall(pattern, st)

print(" ".join(match))


# Cách 2 (vẫn sai nếu chuỗi có dấu chấm tồn tại đơn lẻ)
# t = ''
# for c in st:
#     if c.isdigit() or c == '.': t += c
#     elif t!= '':
#         print(t, end= ' ')
#         t = ''
# print(t)

# Cách 3: (rườm rà)
# t = ''
# i = 0
# st += " "
# while i < len(st):
#     if st[i].isdigit():
#         t += st[i]
#         if st[i+1] == '.':
#             t += '.'
#             i += 1
#     elif t != '':
#         print(t, end= ' ')
#         t =''
#     i += 1