
from database import connect_db
import sqlite3

conn = connect_db()

try:
    while True:
        tenLoaiHang = input("Nhap Ten Loai Hang (nhap q de thoat): ")

        if tenLoaiHang.lower() == "q":
            break

        try:
            conn.execute("""
                INSERT INTO loai_hang (TenLoaiHang)
                VALUES (?)
            """, (tenLoaiHang,))

            conn.commit()
            print("Them loai hang thanh cong!")

        except sqlite3.Error as e:
            conn.rollback()
            print("Loi:", e)

finally:
    conn.close()

