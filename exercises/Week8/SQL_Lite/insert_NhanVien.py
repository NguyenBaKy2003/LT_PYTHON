
from database import connect_db
import sqlite3
from datetime import datetime

conn = connect_db()

try:
    while True:
        ho = input("Nhap ho: ")
        ten = input("Nhap ten: ")

        # Kiem tra dinh dang ngay sinh
        ngaySinh = input("Nhap ngay sinh (DD/MM/YYYY): ")
        try:
            datetime.strptime(ngaySinh, "%d/%m/%Y")
        except ValueError:
            print("Loi: Ngay sinh khong hop le!")
            continue

        # Kiem tra dinh dang ngay lam viec
        ngayLamViec = input("Nhap ngay lam viec (DD/MM/YYYY): ")
        try:
            datetime.strptime(ngayLamViec, "%d/%m/%Y")
        except ValueError:
            print("Loi: Ngay lam viec khong hop le!")
            continue

        diaChi = input("Nhap dia chi: ")

        try:
            luongCoBan = float(input("Nhap luong co ban: "))
            phuCap = float(input("Nhap phu cap: "))
        except ValueError:
            print("Loi: Luong va phu cap phai la so!")
            continue

        try:
            conn.execute("""
                INSERT INTO nhan_vien (
                    Ho, Ten, NgaySinh, NgayLamViec,
                    DiaChi, LuongCoBan, PhuCap
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                ho, ten, ngaySinh, ngayLamViec,
                diaChi, luongCoBan, phuCap
            ))

            conn.commit()
            print("Them Nhan Vien Thanh Cong!")

        except sqlite3.Error as e:
            conn.rollback()
            print("Loi:", e)

        choice = input("Nhap 0 neu muon dung nhap: ")
        if choice == 0:
            break

finally:
    conn.close()
