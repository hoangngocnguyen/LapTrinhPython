# Using employees.csv to hands on
# 1. Convert employee data to dictionary

import csv

"""
    register_dialect: đăng ký một bộ quy tắc với csv.
    skipinitialspace: bỏ qua dấu cách sau dấu phân cách
    strict: báo lỗi khi không đúng format csv
    
    csv.DictReader(open(csv_file_location), dialect='empDialect')
        + Tạo ra một đối tượng dòng
        + Dưới dạng từ điển
        + Dùng dòng đầu tiên làm tiêu đề cột (key, khóa)
        + Áp dụng quy tắc 'empDialect' đã đăng ký
"""

# Định nghĩa hàm đọc nhân viên
def read_employees(csv_file_location):
    # Định nghĩa bộ quy tắc Dialect để đọc ghi File
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

    # Mo File csv, kiểu Dict, theo quy tắc empDialet
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')

    # Trong employee_file: mỗi dòng là một dict

    employee_list = []

    for data in employee_file:
        employee_list.append(data)

    return employee_list


employee_list = read_employees("employees.csv")
print(employee_list)

###########################
###########################
#2.  Process employee data
# Xử lý employee_list: trả về dict đếm số lượng người theo department
###########################
def process_data(employee_list):
    # Lấy ra list department, có lặp lại
    departments = []
    # Duyệt list dict employee_list, lấy department ra, bỏ vào set
    for emp in employee_list:
        departments.append(emp["Department"])

    # Đầu ra là một dict chứa key: department, value: quantity
    employee_data = {}
    # Duyệt danh sách department, ép kiểu qua set
    for department in set(departments):
        # Lấy số lượng
        quantity = departments.count(department)

        # Set giá trị cho dict
        employee_data[department] = quantity

    return employee_data

data = process_data(employee_list)
print(data)


##########################
###########################
# 3. Generate a report: từ dict số lượng -> ghi ra file report.txt
# Format:
# <department1>: <amount1>
# <department2>: <amount2>
#########################
def write_report(employee_data):
    # Mở file
    with open ("report.txt", "w") as report_file:
        # Duyệt dict, ghi file, theo thứ tự
        for key, value in sorted(employee_data.items()):
            report_file.write(f"{key}: {value}\n")

write_report(data)