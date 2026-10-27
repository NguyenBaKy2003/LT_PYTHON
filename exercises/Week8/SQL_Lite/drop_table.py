
import sqlite3
from database import connect_db

conn = connect_db()

try:
    conn.execute("PRAGMA foreign_keys = OFF")

    conn.executescript("""
        DROP TABLE IF EXISTS chi_tiet_dat_hang;
        DROP TABLE IF EXISTS don_dat_hang;
        DROP TABLE IF EXISTS mat_hang;
        DROP TABLE IF EXISTS nha_cung_cap;
        DROP TABLE IF EXISTS loai_hang;
        DROP TABLE IF EXISTS nhan_vien;
        DROP TABLE IF EXISTS khach_hang;
    """)

    conn.commit()
    print("Đã xóa toàn bộ 7 bảng thành công!")

except sqlite3.Error as e:
    conn.rollback()
    print("Lỗi khi xóa bảng:", e)

finally:
    conn.close()
