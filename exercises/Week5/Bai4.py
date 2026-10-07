# Hãy phát triển một chương trình Python cho phép thao tác với file. Hãy mở 1 file và ghi vào đó
# 5 chuỗi văn bản, mỗi chuỗi trên 1 dòng.
# Sau đó hãy đóng file, rồi mở lại file để đọc. Hãy đọc ra 20 byte đầu tiên của file, rồi in ra vị trí
# hiện tại của file đang được đọc.
# Tiếp theo, hãy dịch con trỏ file thêm 10 byte, rồi lại in ra vị trí hiện tại của con trỏ file.


file = open("data.txt", "w", encoding="utf-8")

for i in range(5):
    chuoi = input(f"Nhập chuỗi thứ {i + 1}: ")
    file.write(chuoi + "\n")

file.close()

file = open("data.txt", "r", encoding="utf-8")

noi_dung = file.read(20)

print("\n20 byte đầu tiên của file:")
print(noi_dung)

print("Vị trí hiện tại của con trỏ:", file.tell())

file.seek(file.tell() + 10)

print("Vị trí của con trỏ sau khi dịch thêm 10 byte:", file.tell())

file.close()