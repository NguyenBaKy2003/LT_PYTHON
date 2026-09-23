soLuongPhanTu1 = int(input("Nhap so luong phan tu (it nhat 5): "))
while soLuongPhanTu1 < 5:
    print("So luong phan tu phai it nhat la 5.")
    soLuongPhanTu1 = int(input("Nhap lai so luong phan tu: "))
soLuongPhanTu2 = int(input("Nhap so luong phan tu (it nhat 5): "))
while soLuongPhanTu2 < 5:
    print("So luong phan tu phai it nhat la 5.")
    soLuongPhanTu2 = int(input("Nhap lai so luong phan tu: "))

danhSach1=[]
danhSach2=[]

for i in range(soLuongPhanTu1):
    print("Nhap phan tu thu ", i+1, " cua danh sach 1: ")
    danhSach1.append(int(input()))
for i in range(soLuongPhanTu2):
    print("Nhap phan tu thu ", i+1, " cua danh sach 2: ")
    danhSach2.append(int(input()))

danhSach3=danhSach1+danhSach2

for i in range(1,6):
    print("Danh sach 3: ", danhSach3)
print("Phan tu thu 3 ",danhSach3[2])

print("Phan tu tu 1 den 3: ",danhSach3[1:3])
print("5 phan tu tinh tu ben phai: ", danhSach3[-5:])

tong=0
for i in danhSach3:
    tong+=i
print("Tong cac phan tu trong danh sach 3 la: ", tong)
print("Phan tu lon nhat: ", max(danhSach3))
print("Phan tu nho nhat: ", min(danhSach3))
print("Trung binh cong cac phan tu trong danh sach 3 la: ", tong/len(danhSach3))

