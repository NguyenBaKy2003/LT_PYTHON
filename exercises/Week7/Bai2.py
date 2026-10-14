

# Viết một chương trình cho phép định nghĩa lớp. Tạo ra một lớp có tên là Person, bao
# gồm 3 thuộc tính là name, address và age. Định nghĩa 2 method của lớp này có tên là
# inputDetails() và displayDetails() để cho phép nhập các giá trị cho các thuộc tính, và hiển
# thị giá trị của các thuộc tính của lớp.
# Tiếp theo, hãy khai báo 2 đối tượng của lớp, rồi gọi các method của 2 đối tượng này để
# xem kết quả.


class Person:
    def __init__(self,name = "", address="", age=""):
        self.ten=name
        self.diaChi= address
        self.tuoi= age

    def inputDetails(self):
        self.ten= input("Nhap ten: ")
        self.diaChi=input("Nhap dia chi: ")
        self.tuoi= input("Nhap tuoi: ")
    def displayDetails(self):
        print(f"Ten: {self.ten}, Tuoi: {self.tuoi}, Dia chi: {self.diaChi}")

nv1=Person()
print("Nhap thong tin nhan vien 1")
nv1.inputDetails()

nv2= Person()
print("Nhap thong tin nhan vien 2")
nv2.inputDetails()

print("In ra thong tin ")
nv1.displayDetails()
nv2.displayDetails()

