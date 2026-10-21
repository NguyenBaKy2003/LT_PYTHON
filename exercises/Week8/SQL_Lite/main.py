import sqlite3

conn= sqlite3.Connection("quanly.sql")

print("Ket noi thanh cong")


conn.execute("""
    Crate
""")