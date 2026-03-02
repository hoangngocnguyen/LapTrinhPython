def hop_le(gd):
    ma_sp: str = gd["ma_sp"]
    so_luong: str = gd["so_luong"]
    if len(ma_sp) == 0 or len(so_luong) == 0 or not so_luong.isdigit():
        return False

    return int(so_luong) > 0


def main():
    try:
        # 1. Đọc Q và K
        line1 = input().split()
        if not line1:
            return
        q, k = int(line1[0]), int(line1[1])

        # 2. Đọc chuỗi giao dịch và tách bằng dấu ';'
        raw_input = input().strip()
        if not raw_input:
            return
        raw_data = raw_input.split(';')

        # 3. Tiền xử lý dữ liệu bằng Dictionary để cộng dồn
        stats = {}
        for item in raw_data:
            if ':' not in item:
                continue

            # Làm sạch khoảng trắng thừa theo quy định
            parts = item.split(':')
            if len(parts) != 2:
                continue

            ma_sp = parts[0].strip()
            so_luong_str = parts[1].strip()

            # Kiểm tra tính hợp lệ: Mã không trống, Số lượng là số nguyên dương
            if ma_sp == "":
                continue

            if so_luong_str.isdigit():
                so_luong = int(so_luong_str)
                if so_luong > 0:
                    # Gom nhóm và cộng dồn
                    stats[ma_sp] = stats.get(ma_sp, 0) + so_luong

        # 4. Xử lý các truy vấn Q
        if not stats:
            if q == 2: print("None")
            return

        if q == 1:
            # Tổng số lượng mã sản phẩm duy nhất
            print(len(stats))

        elif q == 2:
            # Lọc danh sách theo K, sắp xếp bảng chữ cái, nối bằng ", "
            rs = [ma for ma, tong in stats.items() if tong >= k]
            if rs:
                rs.sort()
                print(", ".join(rs))
            else:
                print("None")

        elif q == 3:
            # Tìm max
            max_val = max(stats.values())
            # Lấy các mã có cùng giá trị max
            best_sellers = [ma for ma, tong in stats.items() if tong == max_val]
            # Nếu có nhiều mã, lấy mã đầu tiên theo bảng chữ cái
            best_sellers.sort()
            print(f"{best_sellers[0]} {max_val}")

    except (EOFError, ValueError, IndexError):
        pass


if __name__ == "__main__":
    main()