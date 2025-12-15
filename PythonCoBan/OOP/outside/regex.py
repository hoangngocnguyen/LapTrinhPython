import re

message = "Crush cua ban la: Cindy, Yena. Enemy cua ban la Josh"
pattern = r"(: )(\w*, \w+)"
match = re.search(pattern, message)

print(match.group(2))