import re
import sys

st = "He ldhdja He   He"

pattern = r"He*"

rs = re.search(pattern, st)

print(rs)

syslog = sys.argv[0]