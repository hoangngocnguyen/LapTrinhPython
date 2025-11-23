def nhap_ma_tran(hang, cot):
    matrix = [[0 for _ in range(cot)] for _ in range(hang)]
    for i in range(hang):
        for j in range(cot):
            matrix[i][j] = int(input(f"a[{i}][{j}]= "))
    return matrix

def in_ma_tran(matrix):
    for row in matrix:
        for col in row:
            print(f"{col:<7}", end="")
        print()

# Kiểm tra xem ma trận có đối xứng
def is_doi_xung(ma_tran, hang, cot):
    for i in range(hang):
        # print(f"i-{i}")
        for j in range(i, cot):
            # print(f"j-{j}")
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True

# Tính tổng các phần tử trên đường chéo chính
def tong_duong_cheo_chinh(a, hang, cot):
    max = hang if hang < cot else cot
    sum = 0
    for i in range(max):
            sum += a[i][i]

    return sum



