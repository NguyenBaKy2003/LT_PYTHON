# Hãy viết chương trình Python cho phép người dùng hiển thị một menu như hình sau:
# 1. Tính diện tích hình vuông.
# 2. Tính diện tích hình chữ nhật.
# 3. Tính diện tích hình tam giác.
# 4. Tính diện tích hình thang.
# 5. Tính diện tích hình tròn
# 6. Thoát.
# Ứng với mỗi mục trong menu, hãy yêu cầu người dùng nhập các giá trị vào từ bàn phím
# (VD: Chiều dài, chiều rộng ...), sau đó tính toán diện tích và in ra kết quả.


def square_area(side):
    return side * side
def rectangle_area(length, width):
    return length * width
def triangle_area(base, height):
    return 0.5 * base * height
def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height
def circle_area(radius):
    import math
    return math.pi * radius * radius

print("Menu:")
print("1. Tính diện tích hình vuông.")
print("2. Tính diện tích hình chữ nhật.")
print("3. Tính diện tích hình tam giác.")
print("4. Tính diện tích hình thang.")
print("5. Tính diện tích hình tròn.")
print("6. Thoát.")

while True:
    choice = input("Chọn một mục (1-6): ")
    if choice == '1':
        side = float(input("Nhập chiều dài cạnh hình vuông: "))
        print("Diện tích hình vuông là:", square_area(side))
    elif choice == '2':
        length = float(input("Nhập chiều dài hình chữ nhật: "))
        width = float(input("Nhập chiều rộng hình chữ nhật: "))
        print("Diện tích hình chữ nhật là:", rectangle_area(length, width))
    elif choice == '3':
        base = float(input("Nhập độ dài đáy hình tam giác: "))
        height = float(input("Nhập chiều cao hình tam giác: "))
        print("Diện tích hình tam giác là:", triangle_area(base, height))
    elif choice == '4':
        base1 = float(input("Nhập độ dài đáy 1 của hình thang: "))
        base2 = float(input("Nhập độ dài đáy 2 của hình thang: "))
        height = float(input("Nhập chiều cao của hình thang: "))
        print("Diện tích hình thang là:", trapezoid_area(base1, base2, height))
    elif choice == '5':
        radius = float(input("Nhập bán kính hình tròn: "))
        print("Diện tích hình tròn là:", circle_area(radius))
    elif choice == '6':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")