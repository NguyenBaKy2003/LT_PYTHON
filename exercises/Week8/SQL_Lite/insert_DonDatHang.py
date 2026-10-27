from database import connect_db
import sqlite3

conn= connect_db()

try:

    while True:

        maKh= input("Nhap ma khach hang: ")
        maNV= input("Nhap ma nhan vien: ")
        ngayDatHang= input("Nhap ngay dat hang: ")
        ngayGiaoHang= input("Nhap ngay giao hang: ")
        ngayChuyenHang= input("Nhap ngay chuyen hang: ")
        noiGiaoHang= input("Nhap noi giao hang: ")
        try:
            conn.execute(""" Insert into don_dat_hang(MaKH, MaNV, NgayDatHang,NgayGiaoHang, NgayChuyenHang, NoiGiaoHang) \
            Values(?,?,?,?,?,?)
            
""",(maKh,maNV,ngayDatHang,ngayGiaoHang,ngayChuyenHang,noiGiaoHang,))

            conn.commit()
            print("Them don dat hang thanh cong!")
        except sqlite3.Error as e:
            print("Loi: ",e)
            conn.rollback()

        choise= input("Nhap 0 neu muon dung lai: ")
        if choise==0:
            break
            
finally:
    conn.close()
