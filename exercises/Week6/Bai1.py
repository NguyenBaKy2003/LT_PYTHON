# Hãy viết một chương trình Python cho phép cài đặt cơ chế xử lý lỗi. Hãy cài đặt khối try, trong
# đó ta cố tình phát sinh lỗi: ta sẽ in ra giá trị của biến age (biến age này chưa được khai báo). Sau
# đó trong khối except ta sẽ hiển thị thông báo lỗi phù hợp. Đồng thời, ta cũng cài đặt khối finally
# để in ra thông báo kết thúc chương trình.
# Mở rộng: Hãy định nghĩa khối else để hiển thị thông báo khi chương trình thực hiện thành công,
# không có lỗi (bỏ qua khối finally nếu dùng else).


try:
    print(age)

except NameError:
    print("Lỗi: Biến age chưa được khai báo!")

finally:
    print("Kết thúc chương trình.")


try:
    age = 20
    print("Tuổi:", age)

except NameError:
    print("Lỗi: Biến age chưa được khai báo!")

else:
    print("Chương trình thực hiện thành công.")    


try:
    age = 20
    print(age)

except NameError:
    print("Có lỗi xảy ra!")

else:
    print("Chương trình chạy thành công!")

finally:
    print("Kết thúc chương trình.")