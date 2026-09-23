nhapVao=int(input("Nhap vao 1 so: "))
for i in range(1 ,11):
    print(nhapVao, " x ", i, " = ", nhapVao*i)

# in ra tat ca cac so tu 1 den so duoc nhap (buoc nhay 2)

for i in range(1, nhapVao + 1, 2):
    print(i)