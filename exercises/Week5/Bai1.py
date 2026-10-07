# Tạo một chương trình Python cho phép thực hiện những công việc sau:
# - Tạo ra một file text với tên được nhập vào từ bàn phím.
# - Sau đó sử dụng một vòng lặp, nhập 10 dòng văn bản vào file.
# - Đọc ra nội dung của file vừa được ghi.
# - Đếm xem trong file có bao nhiêu dòng có nội dung bắt đầu bằng chuỗi “Tony”
# - Đếm xem trong file có bao nhiêu dòng có nội dung kết thúc bằng chuỗi “Hải”

ten_file = input("Nhập tên file: ")
with open(ten_file, "w", encoding="utf-8") as file:
    for i in range(10):
        dong = input(f"Nhập dòng thứ {i + 1}: ")
        file.write(dong + "\n")


print("\n NỘI DUNG FILE ")

with open(ten_file, "r", encoding="utf-8") as file:
    noi_dung = file.readlines()

for dong in noi_dung:
    print(dong.strip())


dem_bat_dau_tony = 0

dem_ket_thuc_hai = 0

for dong in noi_dung:
    dong = dong.strip()

    if dong.startswith("Tony"):
        dem_bat_dau_tony += 1

    if dong.endswith("Hải"):
        dem_ket_thuc_hai += 1


print("\n KẾT QUẢ ")
print("Số dòng bắt đầu bằng 'Tony':", dem_bat_dau_tony)
print("Số dòng kết thúc bằng 'Hải':", dem_ket_thuc_hai)