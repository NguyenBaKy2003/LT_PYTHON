soPhut=int(input("Nhap so phut: "))
cuocCoBan=27000
# Tinh cuoc
if soPhut<100:
    cuoc= cuocCoBan+ soPhut*120
elif soPhut<200:
    cuoc= cuocCoBan+ 100*120 + (soPhut-100)*110
elif soPhut<300:
    cuoc= cuocCoBan+ 100*120 + 100*110 + (soPhut-200)*100
elif soPhut<400:
    cuoc= cuocCoBan+ 100*120 + 100*110 + 100*100 + (soPhut-300)*80
else: 
    cuoc= cuocCoBan+ 100*120 + 100*110 + 100*100 + 100*80 + (soPhut-400)*40

print("Cuoc dien thoai la: ", cuoc)
thueVAT=cuoc*0.1
print("Thue VAT la: ", thueVAT)
phiVienThong= cuoc*0.05
print("Phi vien thong la: ", phiVienThong)
tongTien= cuoc+thueVAT+phiVienThong
print("Tong so tien phai tra la: ", tongTien)
