# Tạo một chương trình Python cho phép thực hiện những công việc sau:
# - Tạo ra một file text có tên là data.txt.
# - Sau đó sử dụng một vòng lặp, nhập 5 dòng văn bản vào file.
# - Đọc ra nội dung của file vừa được ghi.

with open("data.txt", "w", encoding="utf-8") as file:

    for i in range(5):
        dong = input(f"Nhập dòng thứ {i + 1}: ")
        file.write(dong + "\n")


print("\n NỘI DUNG FILE data.txt ")

with open("data.txt", "r", encoding="utf-8") as file:
    noi_dung = file.read()

print(noi_dung)