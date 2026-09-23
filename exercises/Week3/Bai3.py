# Viết một chương trình cho phép sử dụng hàm. Viết một số hàm sau đây:
# int arearectangle(int a, int b): Dùng để tính diện tích hình chữ nhật
# int square (int x): Dùng để trả về bình phương của một số
# double factorial (int x): Dùng để trả về giai thừa của một số
# Hãy viết và gọi các hàm trên.
def areaRectangle(a,b):
    return a*b
def square(a):
    return a**2
def factorial(a):
    giaiThua=1
    for i in range(1,a+1):
        giaiThua*=i
    return giaiThua

a=int(input("Nhap vao so a: "))
b=int(input("Nhap vao so b: "))
print(areaRectangle(a,b))
print(square(a))
print(factorial(a))
