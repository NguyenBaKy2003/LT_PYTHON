from database import connect_db
conn=connect_db()
import sqlite3
try:
    while True:
        tenCongTy= input("Nhap ten cong ty: ")
        tenGiaoDich= input("Nhap ten giao dich: ")
        diaChi= input("Nhap dia chi: ")
        dienThoai=input("Nhap so dien thoai: ")
        fax= input("Nhap so Fax: ")
        email= input("Nhap email: ")

  
        try:
            conn.execute("""
                INSERT INTO nha_cung_cap(TenCongTy, TenGiaoDich, DiaChi, DienThoai, Fax, Email) \
                Values (?,?,?,?,?,?)""", (tenCongTy,tenGiaoDich,diaChi,dienThoai,fax,email,))
            conn.commit()
            print("Them Nha cung cap thanh cong") 
        except sqlite3.Error as e:
            conn.rollback()
            print("Loi", e)
        choise = int(input("Nhap 0 neu muon dung: "))
        if choise ==0:
            break
        
finally:
    conn.close()