import re

pattern = r"^TIN*"

st = "TIN hocj vawn phong"

match = re.search(pattern, st)

print(match)
