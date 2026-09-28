import quanlydiem

# Tính điểm từng học phần
diem_lap_trinh = quanlydiem.lap_trinh_co_so(8, 7, 9)
diem_tieng_anh = quanlydiem.tieng_anh(7, 8, 8)
diem_phan_tich = quanlydiem.phan_tich_du_lieu(9, 8, 9)

# Xếp loại
diem_tb, xep_loai = quanlydiem.xeploai(
    diem_lap_trinh,
    diem_tieng_anh,
    diem_phan_tich
)

print("Điểm Lập trình cơ sở:", round(diem_lap_trinh, 2))
print("Điểm Tiếng Anh:", round(diem_tieng_anh, 2))
print("Điểm Phân tích dữ liệu:", round(diem_phan_tich, 2))
print("Điểm trung bình:", round(diem_tb, 2))
print("Xếp loại:", xep_loai)