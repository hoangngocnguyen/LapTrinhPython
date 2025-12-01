# Dung Python để thực hiện các lệnh bên ngoài

import subprocess

try:
    ket_qua = subprocess.run(['cmd', '/c', 'dir'], capture_output = True, text = True, check = True)
    print("Mã thoát: ", ket_qua.returncode)
    print("Đầu ra: ", ket_qua.stdout)
except subprocess.CalledProcessError as e:
    print(f"Lệnh thất bại với mã {e.returncode}")
    print("Lỗi: ", e.stderr)


# Chạy tiến trình song song
tien_trinh = subprocess.Popen(['ping', '-c', '4', 'google.com'], stdout=subprocess.PIPE, text=True)

# Lấy đầu ra theo thời gian thực
stdout, sdterr = tien_trinh.communicate()

print("Mã thoát:", tien_trinh.returncode)
print("Đầu ra:\n", stdout)

