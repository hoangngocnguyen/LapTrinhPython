import re

rs = re.search(r"^c", "Co khi nao cho em", re.IGNORECASE)

print(rs[0])

# Lấy 1 từ thỏa regex
print(re.search(r"\w*", "And this is another"))