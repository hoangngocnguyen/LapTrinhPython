# Tao file moi de ghi, bao loi khi da ton tai
try:
    with open("dulieu.txt", "x") as file:
        file.write("Hello world!\n")
except Exception as e:
    print(f"Loi mo file: {e}")

try:
    with open("dulieu.txt", "a") as file:
        file.write("Hello world ghi them!\n")
except Exception as e:
    print(f"Loi mo file: {e}")


with open("dulieu.txt", "w") as file:
    file.write("Hello world ghi de!\n")


with open("dulieu.txt", 'w') as file:
    lst = [1, 2, 3]
    file.write(", ".join(map(str, lst)))

with open("dulieu.txt", 'w', encoding="utf-8") as file:
    file.write("Tôi yêu Cindy")