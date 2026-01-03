# https://coder.husc.edu.vn/problem/nntpy04

def moving_average(data, k):
    """
    Tính trung bình trượt (moving average) của chuỗi dữ liệu theo cửa sổ kích thước k.

    Tham số:
        data (list of float): Chuỗi dữ liệu đầu vào.
        k (int): Kích thước cửa sổ trượt (k ≥ 1).

    Kết quả trả về:
        list of float: Danh sách các giá trị trung bình tương ứng với từng cửa sổ trượt.

    Ghi chú:
        - Nếu k lớn hơn độ dài chuỗi hoặc dữ liệu rỗng, kết quả trả về là danh sách rỗng.
        - Chỉ sử dụng các phép toán cơ bản trên list, không dùng thư viện ngoài.
    """
    if k > len(data) or len(data) == 0:
        return []

    result = []

    # Kiem tra k

    # Duyet qua cac phan tu cua list
    #1 2 3 4 5 6 7 8 ,k = 4
    for i in range(len(data)):
        # Duyet va tinh tong cac phan tu (i -> i + k - 1)
        sum = 0
        for j in range(i, i + k):
            # Neu chi so vuot list -> the bang 0
            value = 0 if j >= len(data) else data[j]
            sum += value

        avg = sum / k
        result.append(avg)

    return result

# ===============================
# Nhập dữ liệu và test hàm
# ===============================

try:
    k = int(input())                       # nhập k
    data = list(map(float, input().split()))        # nhập dãy số thực
except:
    k = 0
    data = []

result = moving_average(data, k)

# In kết quả với 2 chữ số thập phân
print(" ".join(f"{x:.2f}" for x in result))