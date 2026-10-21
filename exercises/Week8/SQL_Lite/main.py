
import sqlite3

conn = sqlite3.connect("quanly.db")

# Bat khoa ngoai
conn.execute("PRAGMA foreign_keys = ON")

print("Ket noi thanh cong")

conn.executescript("""
    CREATE TABLE IF NOT EXISTS khach_hang (
        MaKH INTEGER PRIMARY KEY AUTOINCREMENT,
        TenCongTy TEXT NOT NULL,
        TenGiaoDich TEXT NOT NULL,
        DiaChi TEXT NOT NULL,
        Email TEXT NOT NULL,
        DienThoai TEXT NOT NULL,
        Fax TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS nhan_vien (
        MaNV INTEGER PRIMARY KEY AUTOINCREMENT,
        Ho TEXT NOT NULL,
        Ten TEXT NOT NULL,
        NgaySinh TEXT CHECK (
            NgaySinh IS NULL OR NgaySinh < date('now')
        ),
        NgayLamViec TEXT,
        DiaChi TEXT NOT NULL,
        LuongCoBan REAL NOT NULL CHECK (LuongCoBan > 0),
        PhuCap REAL CHECK (PhuCap >= 0)
    );

    CREATE TABLE IF NOT EXISTS loai_hang (
        MaLoaiHang INTEGER PRIMARY KEY AUTOINCREMENT,
        TenLoaiHang TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS nha_cung_cap (
        MaCT INTEGER PRIMARY KEY AUTOINCREMENT,
        TenCongTy TEXT NOT NULL,
        TenGiaoDich TEXT NOT NULL,
        DiaChi TEXT NOT NULL,
        DienThoai TEXT NOT NULL,
        Fax TEXT NOT NULL,
        Email TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS mat_hang (
        MaHang INTEGER PRIMARY KEY AUTOINCREMENT,
        TenHang TEXT NOT NULL,
        MaCT INTEGER NOT NULL,
        MaLoaiHang INTEGER NOT NULL,
        SoLuong INTEGER CHECK (SoLuong >= 0),
        DonViTinh TEXT NOT NULL,
        GiaHang REAL CHECK (GiaHang > 0),
        FOREIGN KEY (MaLoaiHang)
            REFERENCES loai_hang(MaLoaiHang),
        FOREIGN KEY (MaCT)
            REFERENCES nha_cung_cap(MaCT)
    );

    CREATE TABLE IF NOT EXISTS don_dat_hang (
        SoHoaDon INTEGER PRIMARY KEY AUTOINCREMENT,
        MaKH INTEGER NOT NULL,
        MaNV INTEGER NOT NULL,
        NgayDatHang TEXT NOT NULL DEFAULT (date('now')),
        NgayGiaoHang TEXT,
        NgayChuyenHang TEXT,
        NoiGiaoHang TEXT,
        FOREIGN KEY (MaKH)
            REFERENCES khach_hang(MaKH),
        FOREIGN KEY (MaNV)
            REFERENCES nhan_vien(MaNV)
    );

    CREATE TABLE IF NOT EXISTS chi_tiet_dat_hang (
        MaHang INTEGER NOT NULL,
        SoHoaDon INTEGER NOT NULL,
        GiaBan REAL CHECK (GiaBan > 0),
        SoLuong INTEGER CHECK (SoLuong > 0),
        MucGiamGia REAL DEFAULT 0
            CHECK (MucGiamGia >= 0 AND MucGiamGia <= 1),
        PRIMARY KEY (MaHang, SoHoaDon),
        FOREIGN KEY (SoHoaDon)
            REFERENCES don_dat_hang(SoHoaDon),
        FOREIGN KEY (MaHang)
            REFERENCES mat_hang(MaHang)
    );
""")

conn.commit()
print("Tao bang thanh cong")

conn.close()
