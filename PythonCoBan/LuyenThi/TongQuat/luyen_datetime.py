from datetime import datetime

d1 = datetime(2026, 11, 19, 23, 22, 11)

print(d1.strftime("%d/%m/%Y %H/%M/%S"))

a = 1
b = 2
a, b = b, a

print(a, b)