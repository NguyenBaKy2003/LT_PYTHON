
import sqlite3
from database import connect_db


def nhap_toan_bo_du_lieu():
    conn = connect_db()

    try:
        conn.execute("PRAGMA foreign_keys = ON")

        # 1. KHACH_HANG
        conn.executemany("""
            INSERT INTO khach_hang
            (MaKH, TenCongTy, TenGiaoDich, DiaChi, Email, DienThoai, Fax)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, "A", "A", "12 Nguyễn Sinh Cung", "a@yahoo.com",
             "054.523456", "054.523457"),
            (2, "B", "B", "34 Nguyễn Thiện Thuật", "b@yahoo.com",
             "060.123456", "060.123457"),
            (3, "C", "C", "67/3 Lê Hữu Trác", "c@yahoo.com",
             "0511.876564", "0511.876566"),
            (4, "D", "D", "234/23 Lê Văn Hưu", "d@yahoo.com",
             "061.567894", "061.567898"),
            (5, "E", "E", "12 Nguyễn Văn Linh", "e@yahoo.com",
             "054.826456", "054.826456"),
            (6, "F", "F", "123 Lê Quý Đôn", "f@yahoo.com",
             "054.826456", "054.826456"),
        ])

        # 2. LOAI_HANG
        conn.executemany("""
            INSERT INTO loai_hang (MaLoaiHang, TenLoaiHang)
            VALUES (?, ?)
        """, [
            (1, "A"),
            (2, "B"),
            (3, "C"),
            (4, "D"),
            (5, "E"),
            (6, "F"),
        ])

        # 3. NHA_CUNG_CAP
        conn.executemany("""
            INSERT INTO nha_cung_cap
            (MaCT, TenCongTy, TenGiaoDich, DiaChi,
             DienThoai, Fax, Email)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, "AB", "AB", "12 Trần Hưng Đạo",
             "0511.1234567", "0511.1234568", "ab@yahoo.com"),
            (2, "AC", "AC", "123/5 Lê Văn Hưu",
             "0510.1344567", "0510.1344568", "ac@yahoo.com"),
            (3, "AD", "AD", "12 Lê Duẩn",
             "054.541239", "054.541239", "ad@yahoo.com"),
            (4, "A", "A", "2/1 Trần Hưng Đạo",
             "054.528678", "054.528678", "a@yahoo.com"),
            (5, "B", "B", "30 Trần Hưng Đạo",
             "0511.8234567", "0511.8234567", "b@yahoo.com"),
            (6, "H", "H", "5 Lê Thánh Tôn",
             "0510.8734567", "0510.8734567", "h@yahoo.com"),
        ])

        # 4. NHAN_VIEN
        # Dữ liệu nhân viên trong đề bài bị lệch cột.
        # Cần đối chiếu lại trước khi chạy phần này.

# NHAN_VIEN
        conn.executemany("""
            INSERT INTO nhan_vien
            (MaNV, Ho, Ten, NgaySinh, NgayLamViec,
            DiaChi, LuongCoBan, PhuCap)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, "Nguyễn", "Văn Phú", "12/12/1958",
            "01/11/1978", "245 Lê Văn Hưu", 1456789, 456589),
            (2, "Dương", "Lê Đại", "01/01/1934",
            "23/01/1960", "123 Lê Văn Hưu", 24564564, 787788),
            (3, "Phan Văn", "Hùng", "23/11/1968",
            "01/10/1980", "12/4 Lê Văn Hưu", 12312341, 686668),
            (4, "Nguyễn Văn", "Thành", "12/12/1965",
            "01/10/1985", "1234 Lê Duẩn", 35454545, 454454),
            (5, "Lê Khánh", "Đạt", "31/07/1948",
            "01/10/1965", "12 ABC", 44353555, 445444),
            (6, "Nguyễn Thị", "Huyền", "23/12/1960",
            "01/01/1980", "23 BC", 23242342, 454544),
        ])

        # 5. MAT_HANG
        conn.executemany("""
            INSERT INTO mat_hang
            (MaHang, TenHang, MaCT, MaLoaiHang,
             SoLuong, DonViTinh, GiaHang)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, "Đĩa cứng", 1, 1, 28, "cái", 4000000),
            (2, "Đĩa mềm", 2, 2, 245, "cái", 5000),
            (3, "Cổng USB", 1, 3, 21, "cái", 250000),
            (4, "Màn hình", 3, 4, 5, "cái", 2000000),
            (5, "Bàn phím", 4, 5, 45, "cái", 100000),
            (6, "Đĩa CD", 5, 6, 58, "cái", 3000),
        ])

        # 6. DON_DAT_HANG
        conn.executemany("""
            INSERT INTO don_dat_hang
            (SoHoaDon, MaKH, MaNV, NgayDatHang,
             NgayGiaoHang, NgayChuyenHang, NoiGiaoHang)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, 1, 1, "12/05/2005", "18/05/2005",
             "18/05/2005", "Nguyễn Sinh Cung"),
            (2, 2, 4, "13/12/2005", "17/01/2006",
             None, "Nguyễn Thiện Thuật"),
            (3, 4, 1, "01/10/2005", "02/10/2005",
             None, "Huế"),
            (4, 5, 2, "23/10/2005", "01/11/2005",
             None, "Đà Nẵng"),
            (5, 1, 1, "28/07/1998", "29/07/1998",
             "29/07/1998", "Sài Gòn"),
            (6, 2, 2, "01/01/2000", "02/01/2000",
             None, "Nha Trang"),
        ])

        # 7. CHI_TIET_DAT_HANG
       
        conn.executemany("""
            INSERT INTO chi_tiet_dat_hang
            (MaHang, SoHoaDon, GiaBan, SoLuong, MucGiamGia)
            VALUES (?, ?, ?, ?, ?)
        """, [
            (1, 1, 4200000, 2, 0.1),
            (2, 1, 8000, 12, 0.05),
            (2, 2, 8000, 2, 0.05),
            (3, 3, 300000, 5, 0),
        ])


        conn.commit()
        print("Đã nhập dữ liệu thành công!")

    except sqlite3.Error as e:
        conn.rollback()
        print("Lỗi khi nhập dữ liệu:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    nhap_toan_bo_du_lieu()
