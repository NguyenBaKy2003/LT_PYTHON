soLuongPhanTu=int(input("Nhap so luong phan tu: "))
danhSach=[]
for i in range(soLuongPhanTu):
    print("Nhap phan tu thu ", i+1, ": ")
    danhSach.append(input())
tong=0
for i in danhSach:
    print(i)
    tong+=int(i)

print("Tong cac phan tu trong danh sach la:", tong)
print(len(danhSach))
print(max(danhSach))
print(sorted(danhSach))
# xoa phan tu co chi so la 2

del danhSach[2]
print(danhSach)
del danhSach
