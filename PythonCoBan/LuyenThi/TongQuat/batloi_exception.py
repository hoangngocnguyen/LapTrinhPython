def deptrai(value):
    if value < 0:
        raise ValueError("Quá xấu")
    print("Đẹp trai quá")

### try-except đầy đủ
try:
    deptrai(-1)
except Exception as e:
    print("co loi", e, "type", type(e).__name__)
else:
    ## Chạy khi không có lỗi (try thành công)
    print("Mọi thứ êm trôi")
finally:
    ## Luôn chạy (đóng file, dọn dẹp, đóng db...)
    print("Kết thúc")

