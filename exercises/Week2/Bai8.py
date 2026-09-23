soLuongPhanTu = int(input("Nhap so luong phan tu (it nhat 5): "))
while soLuongPhanTu < 5:
    print("So luong phan tu phai it nhat la 5.")
    soLuongPhanTu = int(input("Nhap lai so luong phan tu: "))

danhSach=[]
for i in range(soLuongPhanTu):
    print("Nhap phan tu thu ", i+1, ": ")
    danhSach.append(input())

print("Phan tu co chi so 4 la: ", danhSach[4])
for i in danhSach:
    print(i)
danhSach[3]="Ghe Hap Sa"
for i in danhSach:
    if i=="Tom Hum Bo Lo PhoMai":
        print("Da thay Tom Hum Bo Lo PhoMai")
        break
danhSach.append("Cua Rang Me")
danhSach2=["Tom Mu Ni Bo Lo PhoMai","Muc Mot Nang Nuong BBQ","Nhum Bien Nuong Mo Hanh"]
danhSach3=danhSach+danhSach2
danhSach3.sort()
for i in danhSach3:
    print(i)
