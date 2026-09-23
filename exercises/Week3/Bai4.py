# Viết một chương trình cho phép định nghĩa một hàm nhận 3 tham số thuộc kiểu số
# nguyên. Hàm này sẽ trả về số lớn nhất trong 3 số đó (3 số sẽ được nhập vào từ bàn
# phím).
# Viết một chương trình cho phép định nghĩa một hàm nhận vào 4 tham số thuộc kiểu số
# thực. Hàm này sẽ trả về trung bình cộng của 4 tham số này (giá trị của 4 số sẽ được nhập
# vào từ bàn phím).


def max3(a,b,c):
    return max(a,b,c)
def avg4(a,b,c,d):
    return (a+b+c+d)/4

a=int(input("Nhap vao so a: "))
b=int(input("Nhap vao so b: "))
c=int(input("Nhap vao so c: "))
d=int(input("Nhap vao so d: "))

print(max3(a,b,c))
print(avg4(a,b,c,d))