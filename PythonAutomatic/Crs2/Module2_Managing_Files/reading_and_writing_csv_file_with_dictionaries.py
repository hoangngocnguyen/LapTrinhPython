import csv

# Đọc file software.csv theo kiểu từ điển (key - value)
with open ("software.csv") as software:
    # Tạo dối tượng đọc file kiểu từ điển
    reader = csv.DictReader(software)
    for row in reader:
        print(f"{row["name"]} has {row["users"]} users")


users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"} ,
{"name": "Josh", "username": "jos", "department": "Designer"}

]
keys = ["name", "username", "department"]
# Ghi vào file by_department.csv: 3 cột, mỗi hàng ứng với 1 dictionary

with open("by_department.csv", "w", newline="") as by_department:
    # Tao doi tuong ghi dictionary
    write = csv.DictWriter(by_department, fieldnames=keys)

    write.writeheader()

    write.writerows(users)

    



