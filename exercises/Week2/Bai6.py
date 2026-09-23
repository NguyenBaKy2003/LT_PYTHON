tong = 0
tongBinhPhuong = 0

i=1
while i <= 100:
    if i == 70:
        print("Khong tinh 70")
        i += 1
        continue
    tong += i
    tongBinhPhuong += i ** 2
    if i == 50:
        print("Tong tu 1 den 50 la: ", tong)
    i += 1
else:
    print("Tong tu 1 den 100 la: ", tong)
    print("Tong binh phuong tu 1 den 100 la: ", tongBinhPhuong)
# Bai 2
z=0
while z < 200:
    z += 1
    if z == 150:
        print("Da den 150, ket thuc")
        break
    if z % 3 == 0:
        continue
    print(z)
