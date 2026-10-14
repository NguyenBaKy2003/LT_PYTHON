# Viết một chương trình Python cho phép tính diện tích và chu vi của các hình học
# như sau:
# 1. Tính diện tích và chu vi hình chữ nhật.
# 2. Tính diện tích và chu vi hình vuông.
# 3. Tính diện tích và chu vi hình tròn.
# 4. Tính diện tích và chu vi hình tam giác
# 5. Thoát.
# Chương trình sẽ được thể hiện theo dạng menu, cần tạo ra các class thể hiện các
# hình trên, mỗi class sẽ bao gồm một constructor cho phép truyền vào các tham số
# cần thiết, VD như hình chữ nhật sẽ bao gồm 2 tham số là chiều dài và chiều rộng.
# Mỗi một class sẽ bao gồm một method tính diện tích và một method tính chu vi.
# Hãy thực thi chương trình và in kết quả.

import math
class HinhHoc: 
    def tinhDienTich(self):
        pass

    def tinhChuVi(self):
        pass

class HinhChuNhat(HinhHoc):
    def  __init__(self, dai="", rong=""):
        self.dai= dai
        self.rong=rong

    def  tinhDienTich(self):
        return self.dai* self.rong
    def  tinhChuVi(self):
        return (self.rong + self.dai)*2

class HinhVuong(HinhHoc):
    def __init__(self, canhA=""):
        self.canhA= canhA
    def tinhDienTich(self):
        return self.canhA**2
    def tinhChuVi(self):
        return self.canhA*4

class HinhTron(HinhHoc):
    
    def __init__(self, banKinh=""):
        self.banKinh=banKinh

    def tinhDienTich(self):
        pi= math.pi
        return pi*(self.banKinh**2)
    def tinhChuVi(self):
        pi= math.pi
        return 2*pi*self.banKinh
class HinhTamGiac(HinhHoc):
    def __init__(self,canhA=" ", canhB="", canhC=""):
        self.canhA= canhA
        self.canhB= canhB
        self.canhC=canhC
    def tinhChuVi(self):
        return self.canhA+self.canhB +self.canhC
    def tinhDienTich(self):
        p= self.tinhChuVi()/2
        return math.sqrt(p*(p-self.canhA) * (p-self.canhB) * (p-self.canhC))

def in_ket_qua(hinh):
    print("\n--- KẾT QUẢ ---")
    print(f"Dien tich: {hinh.tinhDienTich(): }")
    print(f"Chu vi: {hinh.tinhChuVi(): }")
    print("----------------")

def main():
    while  True:
        print("\n===== MENU TÍNH DIỆN TÍCH & CHU VI =====")
        print("1. Tính diện tích và chu vi hình chữ nhật")
        print("2. Tính diện tích và chu vi hình vuông")
        print("3. Tính diện tích và chu vi hình tròn")
        print("4. Tính diện tích và chu vi hình tam giác")
        print("5. Thoát")

        choice= int(input("Nhap vao lua chon: "))

        match choice:
            case 1:
                dai=float(input("Nhap chieu dai: "))
                rong=float(input("Nhap chieu rong: "))
                hinhChuNhat= HinhChuNhat(dai,rong)
                in_ket_qua(hinhChuNhat)

            case 2:
                canhA= float(input("Nhap do dai canh cua hinh vuong: "))
                hinhVuong= HinhVuong(canhA)
                in_ket_qua(hinhVuong)

            case 3:
                banKinh= float(input("Nhap ban kinh hinh tron: "))
                hinhTron= HinhTron(banKinh)
                in_ket_qua(hinhTron)
            case 4:
                canhA= float(input("Nhap do dai canh A cua hinh tam giac: "))
                canhB= float(input("Nhap do dai canh B cua hinh tam giac: "))
                canhC= float(input("Nhap do dai canh C cua hinh tam giac: "))
                hinhTamGiac= HinhTamGiac(canhA, canhB, canhC)
                in_ket_qua(hinhTamGiac)
            case 5: 
                break

if __name__ == "__main__":
    main()


