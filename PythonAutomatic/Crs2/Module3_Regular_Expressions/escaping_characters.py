# Thoát ký tự, dùng để đảo ngược vai trò của ký tự
import re

### Thoát, chuyển regex -> ký tự thường
# Trả về bình thường
print(re.search(r".com", "welcome"))

# Thoát (esc) dấu chấm (\.) nên dấu chấm vẫn tính trong capturing
print(re.search(r"\.com", "welcome"))

# Trả về .com vì dấu chấm vẫn tính trong capturing
print(re.search(r"\.com", "mydomain.com"))


### Thoát w, chuyển vai trò chữ -> regex (lấy word)
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

# w là một chữ bình thường: wwwww -> ''
print(re.search(r"w*", "And_this_is_another"))
