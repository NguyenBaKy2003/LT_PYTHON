import math
# Chu Nhat
print("Nhap chieu Dai: ")
chieuDai= float(input())
print("Nhap chieu rong: ")
chieuRong= float(input())

chuVi=(chieuDai+chieuRong)*2
dienTich=chieuRong*chieuDai

print("Chu vi: ",chuVi)
print("Dien tich: ", dienTich)


# Tam Giac
print("Nhap canh A: ")
canhA=float(input())
print("Nhap canh B: ")
canhB=float(input())
print("Nhap canh C: ")
canhC=float(input())
print("Nhap chieu cao: ")
chieuCao=float(input())
chuViTamGiac=canhA+canhB+canhC
dienTichTamGiac= (canhA*chieuCao)/2
print("Chu vi Tam Giac: ",chuViTamGiac)
print("Dien tich Tam Giac: ", dienTichTamGiac)

#  Hinh Tron
print("Nhap ban kinh: ")
banKinh=float(input())
chuViHTron= 2* banKinh * math.pi
dienTichHTron= math.pi*(banKinh**2)
print("Chu vi Hinh Tron: ",chuViHTron)
print("Dien tich Hinh Tron: ", dienTichHTron)

#  Hinh Vuong
print("Nhap canh hinh vuong: ")
canhHVuong=float(input())
chuViHVuong=4*canhHVuong
dienTichHVuong= canhHVuong**2
print("Chu vi Hinh Vuong: ",chuViHVuong)
print("Dien tich Hinh Vuong: ", dienTichHVuong)

# Hinh Thang
print("Nhap canh ben A: ")
canhBenA=float(input())
print("Nhap canh ben B: ")
canhBenB=float(input())
print("Nhap day lon: ")
dayLon=float(input())
print("Nhap day be: ")
dayBe=float(input())
print("Nhap chieu cao hinh thang: ")
chieuCaoHThang=float(input())
chuViHThang= canhBenA+canhBenB+dayLon+dayBe
dienTichHThang= ((dayBe+dayLon)*chieuCaoHThang)/2

print("Chu vi Hinh Thang: ",chuViHThang)
print("Dien tich Hinh Thang: ", dienTichHThang)


