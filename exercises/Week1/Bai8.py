soDien=float(input("Nhap vao so dien: "))
giaDienCoBan=450

if soDien<=100:
    tienDien=soDien*giaDienCoBan
elif soDien<=200:
    tienDien=100*giaDienCoBan+ (soDien-100)*600
elif soDien<=300:
    tienDien=100*giaDienCoBan+ 100*600+ (soDien-200)*750
elif soDien<=500:
    tienDien=100*giaDienCoBan+ 100*600+ 100*750 + (soDien-300)*900
elif soDien<=1000:
    tienDien=100*giaDienCoBan+ 100*600+ 100*750+200*900 +(soDien-500)*1000
else:
    tienDien= 100*giaDienCoBan+ 100*600+ 100*750+200*900 + 500*1000 +(soDien-1000)*1200

print("Tien Dien truoc thue: ", tienDien)
vat=tienDien*0.1
tongTien= tienDien+vat
print("Tong so tien dien sau thue la: ", tongTien)