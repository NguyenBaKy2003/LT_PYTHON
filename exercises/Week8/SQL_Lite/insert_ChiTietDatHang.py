from database import connect_db
import sqlite3

conn=connect_db()

try:

    while True:
        soHoaDon= input("Nhap so hoa don: ")
        maHang= input("Nhap ma hang: ")
        giaBan= input("Nhap gia ban: ")
        soLuong= input("Nhap so luong: ")
        mucGiamGia= input("Nhap muc giam gia: ")
        try:
            conn.execute(""" Insert Into chi_tiet_dat_hang(SoHoaDon,MaHang,GiaBan, SoLuong, MucGiamGia) \
            Values(?,?,?,?,?)
""",(soHoaDon,maHang, giaBan,soLuong,mucGiamGia,))
            conn.commit()
            print("Them Chi Tiet Don Thanh Cong! ")
        except sqlite3.Error as e:
            conn.rollback()
            print("Loi: ",e)

        choise=input("Nhap 0 neu muon dung lai:")
        if choise==0:
            break

finally:
    conn.close()

