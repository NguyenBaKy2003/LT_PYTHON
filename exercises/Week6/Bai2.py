# Viết một chương trình Python cho phép kiểm tra nhiều loại ngoại lệ trong chương trình.
# Hãy gán giá trị cho một biến chưa được khai báo.
# Hãy khai báo một danh sách gồm 4 phần tử, rồi truy cập đến phần tử thứ 6 trong danh
# sách.
# Hãy chia một số cho 0.
# Sau đó hãy định nghĩa nhiều khối except, mỗi khối cài đặt xử lý một loại ngoại lệ riêng
# biệt.
# Hãy định nghĩa khối finally để hiển thị thông báo thành công.
# Hãy thực thi chương trình để kiểm tra kết quả của các loại ngoại lệ

try:
    age = age + 1
except NameError:
    print("Lỗi 1: Biến age chưa được khai báo!")

try:
    danh_sach = [10, 20, 30, 40]
    print(danh_sach[5])
except IndexError:
    print("Lỗi 2: Danh sách không có phần tử thứ 6!")

try:
    a = 10
    b = 0
    ket_qua = a / b
    print(ket_qua)
except ZeroDivisionError:
    print("Lỗi 3: Không thể chia một số cho 0!")

finally:
    print("Kết thúc kiểm tra ngoại lệ.")
