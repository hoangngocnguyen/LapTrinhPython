import csv

# Open csv_file.txt
f = open("csv_file.txt")

# Đọc file theo dạng csv
csv_f = csv.reader(f)

# Duyệt từng dòng và in ra
for row in csv_f:
    # Ánh xạ các giá trị từ đối tượng "row"
    name, phone, role = row
    print(f"Name: {name}, Phone: {phone}, Role: {role}")

# Close file
f.close()
