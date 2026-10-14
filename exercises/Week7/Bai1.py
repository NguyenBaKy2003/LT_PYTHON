# model

class NhanVien:
    def __init__(self,id,name,salary):
        self.ma=id
        self.ten=name
        self.luong= salary
    def display(self):
        print('id = ',self.ma)
        print('ten = ',self.ten)
        print('luong = ',self.luong)
nv1= NhanVien(1,"Tieu Vy",1000)
nv1.display()
nv2= NhanVien(2,'Tran Khon', 2000)
nv2.display()