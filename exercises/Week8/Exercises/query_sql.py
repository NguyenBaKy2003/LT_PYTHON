
import sqlite3

def truy_van_database():
    conn = sqlite3.connect("quanlysinhvien.db")
    conn.execute("PRAGMA foreign_keys = ON")

    try:
        # 1. In 3 sinh viên có học bổng cao nhất
        print("\n1. Top 3 sinh viên có học bổng cao nhất:")

        rows = conn.execute("""
            SELECT MaSV, HoSV, TenSV, HocBong
            FROM sinh_vien
            ORDER BY HocBong DESC
            LIMIT 3
        """).fetchall()

        for row in rows:
            print(row)

        # 2. Tìm sinh viên có tên bắt đầu bằng chữ T
        print("\n2. Sinh viên có tên bắt đầu bằng chữ T:")

        rows = conn.execute("""
            SELECT *
            FROM sinh_vien
            WHERE TenSV LIKE 'T%'
        """).fetchall()

        for row in rows:
            print(row)

        # 3. Cập nhật sinh viên A05 thành Tony Nguyễn
        print("\n3. Cập nhật sinh viên A05:")

        cursor = conn.execute("""
            UPDATE sinh_vien
            SET HoSV = 'Tony', TenSV = 'Nguyễn'
            WHERE MaSV = 'A05'
        """)

        if cursor.rowcount > 0:
            print("Đã cập nhật sinh viên A05.")
        else:
            print("Không tìm thấy sinh viên A05.")

        conn.commit()

        # 4. Xóa sinh viên có học bổng bằng 0
        print("\n4. Xóa sinh viên có học bổng bằng 0:")

        conn.execute("""
            DELETE FROM ket_qua
            WHERE MaSV IN (
                SELECT MaSV
                FROM sinh_vien
                WHERE HocBong = 0
            )
        """)

        cursor = conn.execute("""
            DELETE FROM sinh_vien
            WHERE HocBong = 0
        """)

        print(f"Đã xóa {cursor.rowcount} sinh viên.")
        conn.commit()

        # 5. Hiển thị danh sách sinh viên sau khi cập nhật
        print("\n5. Danh sách sinh viên sau khi xử lý:")

        rows = conn.execute("""
            SELECT *
            FROM sinh_vien
        """).fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        conn.rollback()
        print("Lỗi:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    truy_van_database()
