
import sqlite3

conn = sqlite3.connect("quanlysinhvien.db")
conn.execute("PRAGMA foreign_keys = ON")

print("Kết nối thành công")

try:
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS khoa (
            MaKH TEXT(2) PRIMARY KEY NOT NULL,
            TenKH TEXT(50) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS mon_hoc (
            MaMH TEXT(2) PRIMARY KEY NOT NULL,
            TenMH TEXT(25) NOT NULL,
            SoTiet INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS sinh_vien (
            MaSV TEXT(3) PRIMARY KEY NOT NULL,
            HoSV TEXT(15) NOT NULL,
            TenSV TEXT(7) NOT NULL,
            Phai INTEGER,
            NgaySinh TEXT,
            NoiSinh TEXT,
            MaKH TEXT(2),
            HocBong INTEGER,
            FOREIGN KEY (MaKH) REFERENCES khoa(MaKH)
        );

        CREATE TABLE IF NOT EXISTS ket_qua (
            MaSV TEXT(3) NOT NULL,
            MaMH TEXT(2) NOT NULL,
            Diem REAL NOT NULL,
            PRIMARY KEY (MaSV, MaMH),
            FOREIGN KEY (MaSV) REFERENCES sinh_vien(MaSV),
            FOREIGN KEY (MaMH) REFERENCES mon_hoc(MaMH)
        );
    """)

    conn.commit()
    print("Tạo bảng thành công!")

except sqlite3.Error as e:
    conn.rollback()
    print("Lỗi:", e)

finally:
    conn.close()
