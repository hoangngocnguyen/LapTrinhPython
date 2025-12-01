from datetime import datetime   # import class datetime từ module datetime trực tiếp

x = datetime(2005, 12, 19)

print(x)

# Month name
print(x.strftime("%B"))     # December

# day/month/year (string format)
print(x.strftime("%d/%m/%Y"))


# Format
date_str = "07/07/2025"
format_str = "%d/%m/%Y"

dt_obj = datetime.strptime(date_str, format_str)

print(f"{dt_obj} is later than {x}: {dt_obj > x}")


