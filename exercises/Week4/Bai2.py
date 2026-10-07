from hinhhocnangcao import *




a = float(input("Nhập cạnh a của hình bình hành: "))
b = float(input("Nhập cạnh b của hình bình hành: "))
h = float(input("Nhập chiều cao hình bình hành: "))

print("\n HÌNH BÌNH HÀNH ")
print("Chu vi:", chu_vi_hinh_binh_hanh(a, b))
print("Diện tích:", dien_tich_hinh_binh_hanh(a, h))




r = float(input("\nNhập bán kính hình trụ: "))
h = float(input("Nhập chiều cao hình trụ: "))

print("\n HÌNH TRỤ ")
print("Chu vi đáy:", chu_vi_hinh_tru(r, h))
print("Diện tích toàn phần:", dien_tich_hinh_tru(r, h))


canh = float(input("\nNhập cạnh hình thoi: "))
d1 = float(input("Nhập đường chéo thứ nhất: "))
d2 = float(input("Nhập đường chéo thứ hai: "))

print("\n HÌNH THOI ")
print("Chu vi:", chu_vi_hinh_thoi(canh))
print("Diện tích:", dien_tich_hinh_thoi(d1, d2))



canh = float(input("\nNhập cạnh hình ngũ giác đều: "))

print("\n HÌNH NGŨ GIÁC ĐỀU ")
print("Chu vi:", chu_vi_hinh_ngu_giac_deu(canh))
print("Diện tích:", dien_tich_hinh_ngu_giac_deu(canh))




a = float(input("\nNhập đáy lớn hình thang cân: "))
b = float(input("Nhập đáy nhỏ hình thang cân: "))
c = float(input("Nhập cạnh bên hình thang cân: "))
h = float(input("Nhập chiều cao hình thang cân: "))

print("\n HÌNH THANG CÂN ")
print("Chu vi:", chu_vi_hinh_thang_can(a, b, c))
print("Diện tích:", dien_tich_hinh_thang_can(a, b, h))