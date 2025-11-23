message = "Ma OTP cua ban de kich hoat ngan hang la [191105]"

# Yêu cầu: Lấy ra mã OTP 6 số trong tin nhă cách bởi []
# Cách 1: Sử dụng kiến thức chuỗi
index = message.index("[")

otp = message[index+1:index+7]
print(otp)

# Cách 2: Sử dụng kiến thức regex
import re

# Tạo pattern
regex = r"\[(\d+)]"

# áp dụng pattern vào tìm message
otp = re.search(regex, message)
print(regex)
print(otp)

# Lấy vùng index, lấy giá trị match
print(f"Vùng index:{otp[0]}, giá trị otp: {otp[1]}")