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