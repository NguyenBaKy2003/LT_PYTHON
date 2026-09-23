soCanTinhGiaiThua=int(input("Nhap vao so can tinh giai thua: "))

giaiThua=1
i=1
while(i<soCanTinhGiaiThua):
    i+=1
    giaiThua*=i
else: 
    print("Gia thua cua so ", soCanTinhGiaiThua," la: ",giaiThua)


# 
start=300
while(start<=500):
    if start==400:
        print("Da den 400, ket thuc")
        break
    elif start==350:
        print("Da den 350, bo qua")
        start+=1
        continue
    print(start)
    start+=1
