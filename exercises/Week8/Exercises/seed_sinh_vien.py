
import sqlite3

conn = sqlite3.connect("quanlysinhvien.db")
conn.execute("PRAGMA foreign_keys = ON")

try:
    # Xóa dữ liệu theo thứ tự khóa ngoại
    conn.execute("DELETE FROM ket_qua")
    conn.execute("DELETE FROM sinh_vien")
    conn.execute("DELETE FROM mon_hoc")
    conn.execute("DELETE FROM khoa")

    # 1. Bang KHOA
    conn.executemany("""
        INSERT INTO khoa (MaKH, TenKH)
        VALUES (?, ?)
    """, [
        ("AV", "Anh Văn"),
        ("TH", "Tin Học"),
        ("TR", "Triết")
    ])

    # 2. Bang MON_HOC
    conn.executemany("""
        INSERT INTO mon_hoc (MaMH, TenMH, SoTiet)
        VALUES (?, ?, ?)
    """, [
        ("01", "Cơ sở dữ liệu", 45),
        ("02", "Trí tuệ nhân tạo", 45),
        ("03", "Truyền tin", 45),
        ("04", "Đồ họa", 60),
        ("05", "Văn phạm", 60)
    ])

    # 3. Bang SINH_VIEN
    conn.executemany("""
        INSERT INTO sinh_vien
        (MaSV, HoSV, TenSV, Phai, NgaySinh,
         NoiSinh, MaKH, HocBong)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, [
        ("A01", "Nguyễn thị", "Hải", 1,
         "23/02/1977", "Hà Nội", "TH", 130000),
        ("A02", "Trần văn", "Chính", 0,
         "24/12/1977", "Bình Định", "TH", 150000),
        ("A03", "Lê thu bạch", "Yến", 1,
         "21/02/1977", "Tp HCM", "TH", 170000),
        ("A04", "Trần anh", "Tuấn", 0,
         "20/12/1977", "Hà Nội", "AV", 80000),
        ("B01", "Trần thanh", "Mai", 1,
         "12/08/1977", "Hải Phòng", "TR", 0),
        ("B02", "Trần thị thu", "Thúy", 1,
         "02/01/1979", "Tp HCM", "AV", 0)
    ])

    # 4. Bang KET_QUA
    conn.executemany("""
        INSERT INTO ket_qua (MaSV, MaMH, Diem)
        VALUES (?, ?, ?)
    """, [
        ("A01", "01", 3),
        ("A01", "02", 6),
        ("A01", "03", 5),
        ("A02", "01", 4.5),
        ("A02", "03", 10),
        ("A02", "05", 9),
        ("A03", "01", 2),
        ("A03", "03", 2.5),
        ("A04", "05", 10),
        ("B01", "01", 7),
        ("B01", "03", 2.5),
        ("B02", "02", 6),
        ("B02", "04", 10)
    ])

    conn.commit()
    print("Đã nhập toàn bộ dữ liệu thành công!")

    for table in ["khoa", "mon_hoc", "sinh_vien", "ket_qua"]:
        count = conn.execute(
            f"SELECT COUNT(*) FROM {table}"
        ).fetchone()[0]
        print(f"Bang {table}: {count} bản ghi")

except sqlite3.Error as e:
    conn.rollback()
    print("Lỗi khi nhập dữ liệu:", e)

finally:
    conn.close()
