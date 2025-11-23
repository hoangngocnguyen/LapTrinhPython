import os

lst = os.getenv("Path").split(";")
for item in lst:
    print(item)