import re

# [] hoặc
print(re.search(r"[Pp]ython", "python is the best"))

# [a-z] vùng ký tự
print(re.search(r"c[a-z]ndy", "I love you cindy"))

# None vì ở trước "cindy" phải có 1 ký tự [a-z]
print(re.search(r"[a-z]cindy", "I love you cindy"))

# [] hỗ trợ nhiều vùng ký tự.
print(re.search(r"cind[a-z0-9A-Z]", "cindY is my love"))
print(re.search(r"cind[a-z0-9A-Z]", "cind9 is my love"))


### Circumflex với tập hợp -> Phủ định
# Tìm ký tự không thuộc từ [a-z] và [A-Z] -> dấu chấm
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))

# Không là chữ, không là space -> chỉ có dấu chấm
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

### | hoặc
print(re.search(r"I|You", "I love you"))
print(re.search(r"I|You", "I love Cindy"))
print(re.search(r"I|You", "He love Yous"))

### Tìm tất cả
print(re.findall(r"I|You", "He and I love Yous"))


