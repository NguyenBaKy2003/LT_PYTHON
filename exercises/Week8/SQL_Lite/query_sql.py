

from database import connect_db
conn= connect_db()

# 3. Sử dụng câu lệnh SQL để viết các câu lệnh truy vấn sau đây : 
# a. Hãy chèn tất cả dữ liệu trên vào các bảng trong CSDL. 
# b. Hãy tìm tất cả các khách hàng có mã từ 2-4 
# c. Cập nhật mặt hàng có mã là 1: Đổi tên thành ‘webcam’, giá thành 500000 
# d. Xoá nhà cung cấp có mã là 6 
# e. Tìm ra những mặt hàng có giá < 150000 
# f. Tìm ra những mặt hàng có đơn vị tính >= 20 
# g. Tìm ra những khách hàng có họ ‘Nguyễn’ (bắt đầu bằng từ Nguyễn) 
# Hãy viết chương trình Python có tạo CSDL, tạo các bảng, chèn dữ liệu vào bảng, 
# sau đó thực hiện các câu lệnh trên.
def thu_hien_truy_van():
    # b. Hãy tìm tất cả các khách hàng có mã từ 2-4 
    print("# b. Hãy tìm tất cả các khách hàng có mã từ 2-4 \n")
    khach_hang= conn.execute(""" Select * from khach_hang where MaKH in (2,3,4)""").fetchall()
    for row in khach_hang:
        print(row)
    # c. Cập nhật mặt hàng có mã là 1: Đổi tên thành ‘webcam’, giá thành 500000 
    print("# c. Cập nhật mặt hàng có mã là 1: Đổi tên thành ‘webcam’, giá thành 500000 \n")

    conn.execute(""" Update mat_hang SET TenHang=?, GiaHang=? \
        where MaHang=?
        """, ("webcam",500000,1))
    conn.commit()
    print(conn.execute("""
            SELECT * FROM mat_hang WHERE MaHang = 1
        """).fetchall())

    # d. Xoá nhà cung cấp có mã là 6 
    print(" # d. Xoá nhà cung cấp có mã là 6 \n")
    so_mat_hang = conn.execute("""
            SELECT COUNT(*)
            FROM mat_hang
            WHERE MaCT = 6
        """).fetchone()[0]

    if so_mat_hang == 0:
        conn.execute("""
                DELETE FROM nha_cung_cap
                WHERE MaCT = 6
            """)
        conn.commit()
        print("Đã xóa nhà cung cấp mã 6.")
    else:
        print(
                "Không thể xóa nhà cung cấp mã 6 vì "
                "vẫn có mặt hàng tham chiếu đến nhà cung cấp này."
            )

    # e. Tìm ra những mặt hàng có giá < 150000 
    print(" e. Tìm ra những mặt hàng có giá < 150000 \n")
    rows=conn.execute("select * from mat_hang where GiaHang < 150000").fetchall()
    for row in rows:
        print(row)
    # f. Tìm ra những mặt hàng có đơn vị tính >= 20 
    print("f. Tìm ra những mặt hàng có đơn vị tính >= 20 \n")
    rows=conn.execute("select * from mat_hang where SoLuong>=20").fetchall()
    for row in rows:
        print(row)
    # g. Tìm ra những nhan vien có họ ‘Nguyễn’ (bắt đầu bằng từ Nguyễn) 
    print("g. Tìm ra những nhan vien có họ ‘Nguyễn’ (bắt đầu bằng từ Nguyễn) \n")
    rows=conn.execute("select * from nhan_vien where Ho like 'Nguyễn%' ").fetchall()
    for row in rows:
        print(row)

if __name__=="__main__":
    thu_hien_truy_van()