from database import connect_db
conn= connect_db()

import sqlite3

try:

    while True:

        tenCongTy= input("Nhap ten cong ty: ")
        tenGiaoDich= input("Nhap ten giao dich: ")
        diaChi= input("Nhap dia chi: ")
        email= input("Nhap email: ")
        dienThoai= input("Nhap dien thoai: ")
        fax=input("Nhap so Fax: " )
        try:

            conn.execute("""
insert into khach_hang(TenCongTy, TenGiaoDich, DiaChi, Email,DienThoai,Fax) \
values (?,?,?,?,?,?)
    """,(tenCongTy,tenGiaoDich, diaChi, email, dienThoai, fax,))

            conn.commit()
            print("Them khach hang thanh cong:")
        except sqlite3.Error as e:
            conn.rollback()
            print("Loi", e)
        choise = input("Nhap 0 neu muon dung:  ")
        if choise==0:
            break
    

finally:
    conn.close()