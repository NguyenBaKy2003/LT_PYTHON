
hoTen=input("Nhap ho ten sinh vien: ")
diem=float(input("Nhap diem sinh vien: "))
# diem thuong
if ( 21<=diem<=25):
    diem_thuong=5
elif ( 15<=diem<21):
    diem_thuong=3
elif ( 10<=diem<15):
    diem_thuong=1
else: 
    diem_thuong=0

# xep loai sinh vien

if ( 0<=diem<10):
    xep_loai="D"
elif ( 10<=diem<15):
    xep_loai="C"
elif ( 15<=diem<21):
    xep_loai="B"
elif ( 21<=diem<=25):
    xep_loai="A"
else: 
    xep_loai="Khong xep loai duoc"
print("Sinh vien: ", hoTen)
print("Diem: ", diem)
print("Diem thuong: ", diem_thuong)
print("Xep loai: ", xep_loai)



