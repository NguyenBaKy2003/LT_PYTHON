# Phát triển một chương trình Python cho phép thực hiện các thao tác liên quan đến tập
# tin. Hãy thực hiện các thao tác sau, làm theo menu:
# 1. Ghi file (data.txt)
# 2. Đọc file
# 3. In ra thông tin mô tả về file (tên, mode, closed)
# 4. Đổi tên file thành newdata.txt (sử dụng module os)
# 5. Kết thúc

# Về phần ghi file: Hãy cho phép người dùng nhập vào 5 chuỗi từ bàn phím, rồi ghi 5 chuỗi
# này vào file.

import os





ten_file = "data.txt"

while True:
    print("\n========== MENU ==========")
    print("1. Ghi file (data.txt)")
    print("2. Đọc file")
    print("3. Thông tin file")
    print("4. Đổi tên file thành newdata.txt")
    print("5. Kết thúc")
    print("==========================")

    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == "1":
        with open(ten_file, "w", encoding="utf-8") as file:
            for i in range(5):
                chuoi = input(f"Nhập chuỗi thứ {i + 1}: ")
                file.write(chuoi + "\n")

        print("Đã ghi 5 chuỗi vào file", ten_file)

    elif lua_chon == "2":
        try:
            with open(ten_file, "r", encoding="utf-8") as file:
                noi_dung = file.read()

            print("\n--- NỘI DUNG FILE ---")
            print(noi_dung)

        except FileNotFoundError:
            print("File chưa tồn tại!")

    elif lua_chon == "3":
        try:
            file = open(ten_file, "r", encoding="utf-8")

            print("\n--- THÔNG TIN FILE ---")
            print("Tên file:", file.name)
            print("Mode:", file.mode)
            print("Closed:", file.closed)

            file.close()

            print("Sau khi đóng file:")
            print("Closed:", file.closed)

        except FileNotFoundError:
            print("File chưa tồn tại!")

    elif lua_chon == "4":
        try:
            os.rename(ten_file, "newdata.txt")
            ten_file = "newdata.txt"

            print("Đã đổi tên file thành newdata.txt")

        except FileNotFoundError:
            print("File chưa tồn tại!")

        except FileExistsError:
            print("File newdata.txt đã tồn tại!")

    elif lua_chon == "5":
        print("Chương trình kết thúc.")
        break

    else:
        print("Lựa chọn không hợp lệ!")