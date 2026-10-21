from database import connect_db
conn=connect_db()
import sqlite3

try:
    while True:

        tenHang= input("Nhap ten hang: ")
        maCT= input("Nhap ma cong ty: ")
        maLoaiHang= input("Nhap ma loai hang: ")
        soLuong= input("Nhap so luong: ")
        donViTinh= input("Nhap don vi tinh: ")
        giaHang= input("Nhap gia hang: ")
        try:
            conn.execute("""
    Insert Into mat_hang(TenHang, MaCT, MaLoaiHang, SoLuong, DonViTinh, GiaHang) \
    Values (?,?,?,?,?,?) 
""", (tenHang,maCT, maLoaiHang, soLuong, donViTinh, giaHang,))
            conn.commit()
            print("Them Mat Hang thanh cong!")
        except sqlite3.Error as e:
            conn.rollback()
            print("Loi",e)

        choise = input("Nhap 0 neu muon dung:  ")
        if choise==0:
            break
finally:

    conn.close()