# Bai 1
tong=0
tongBinhPhuong=0
for i in range(1,101):
    tong+=i
    tongBinhPhuong+=i**2
else: 
    print("Tong tu 1 den 100 la: ", tong)
    print("Tong binh phuong tu 1 den 100 la: ", tongBinhPhuong)

# Bai 2
trungBinhCong=0
for i in range(1,101):
    trungBinhCong+=i
else:
    print("Trung binh cong tu 1 den 100 la: ", trungBinhCong/100)
# Bai 3
soCanTinhGiaiThua=int(input("Nhap so can tinh giai thua: "))
giaiThua=1
for i in range(1,soCanTinhGiaiThua+1):
    giaiThua*=i
else:
    print("Giai thua cua so ", soCanTinhGiaiThua, " la: ", giaiThua)
# While
i=1
giaThuaWhile=1
while(i<soCanTinhGiaiThua):
    i+=1
    giaThuaWhile*=i
else: 
    print("Giai thua cua so ", soCanTinhGiaiThua, " la: ", giaThuaWhile)

