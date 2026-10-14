# Viết một chương trình cho phép định nghĩa lớp. Tạo ra một lớp Calculator thể
# hiện máy tính điện tử. Định nghĩa 4 method add(), minus(), devide(), multiple()
# cho phép thể hiện 4 phép tính cơ bản.
# Sau đó hãy định nghĩa method factorial() cho phép tính và in ra giai thừa của
# tham số.
# Tiếp theo hãy khởi tạo một đối tượng của lớp, rồi gọi 4 method của lớp để xem
# kết quả. Chú ý: Hai số được nhập vào từ bàn phím.


class Calculator:

    def __init__(self, a="", b=""):
        self.soA=a
        self.soB=b

    def add(self):
        return self.soA+self.soB
    def minus(self):
        return self.soA-self.soB
    def devide(self):
        if self.soB==0:
                    return "Khong the chia cho 0"
        return self.soA / self.soB
    def multiple(self):
        
        return self.soA*self.soB

    def factorial(self, n):
        if n<0:
            return "Khong gia thua so be hon 0"
        if n==1 or n==0:
            return 1
        else: 
            giaiThua=1
            for i in range (1,n+1):
                giaiThua= giaiThua*i 
            return giaiThua


a=float(input("Nhap vao so A: "))
b=float(input("Nhap vao so B: "))

calc= Calculator(a,b)

print(f"Tong {calc.soA} + {calc.soB} = {calc.add()}")
print(f"Hieu {calc.soA} - {calc.soB} = {calc.minus()}")
print(f"Chia {calc.soA} / {calc.soB} = {calc.devide()}")
print(f"Nhan {calc.soA} * {calc.soB} = {calc.multiple()}")

giaiThua= int(input("Nhap so can tinh giai thua: "))
print(f"Giai thua cua {giaiThua} la : {calc.factorial(giaiThua)}")

