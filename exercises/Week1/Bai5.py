soNguyen=int(input("Nhap so can kiem tra: "))
if (soNguyen%2==0):
    print("So chan")
else:
    print("So le")

soGio=float(input("Nhap vao so gio lam trong tuan: "))
luongTrenGio=2
if(soGio<=40):
    tongLuong= soGio*luongTrenGio
    print("Luong bang: ",tongLuong)
else:
    tongLuong=soGio*luongTrenGio*1.5
    print("Luong banh: ", tongLuong)
    