# Hãy viết một chương trình Python cho phép tạo ra các class như hình sau, đồng thời in ra
# các giá trị của các thuộc tính.

# Hãy định nghĩa các class với các thuộc tính và phương thức như hình trên, sau đó hãy
# khởi tạo các đối tượng của các lớp, rồi hiển thị giá trị của các thuộc tính đó, cũng như gọi
# các phương thức của các đối tượng.
# Chú ý: Các lớp có kế thừa lẫn nhau như sơ đồ trên.


class Vehicle:
    def __init__(self,name,maxPassengers, maxSpeed):
        self.name=name
        self.maxPassengers=maxPassengers
        self.maxSpeed= maxSpeed

class LandVehicle(Vehicle):

    def __init__(self,numWheels, name, maxPassengers, maxSpeed):
        self.numWheels= numWheels
        super().__init__(name, maxPassengers, maxSpeed)
    def drive(self):
        print(f"{self.name} đang chạy trên đất liền bằng {self.numWheels} bánh.")

class SeaVessel(Vehicle):
    def __init__(self,displacement, name, maxPassengers, maxSpeed):
        self.displacement= displacement
        super().__init__(name, maxPassengers, maxSpeed)
    def launch(self):
         print(f"{self.name} với lượng giãn nước {self.displacement} tấn đã hạ thủy.")

class Jeep(LandVehicle):
    def __init__(self, numWheels, name, maxPassengers, maxSpeed):
        super().__init__(numWheels, name, maxPassengers, maxSpeed)
    def soundHorn(self):
         print(f"[{self.name} còi kêu]: Bíp bíp! Hello Jeep")
class Hovercraft(LandVehicle, SeaVessel):
    def __init__(self, numWheels, displacement, name, maxPassengers, maxSpeed):

        LandVehicle.__init__(self, numWheels, name, maxPassengers, maxSpeed)
        SeaVessel.__init__(self, displacement, name, maxPassengers, maxSpeed)

    def enterLand(self):
        print(f"{self.name} đang chuyển sang chế độ di chuyển trên đất liền.")
    def enterSea(self):
                print(f"{self.name} đang chuyển sang chế độ di chuyển trên mặt nước.")

class Frigate(SeaVessel):
    def  __init__(self, displacement, name, maxPassengers, maxSpeed):
        super().__init__(displacement, name, maxPassengers, maxSpeed)
    def fireGun(self):
        print(f"[{self.name} khai hỏa]: Đoành! Đoành! Bang Bang")
xe_jeep = Jeep(numWheels=4, name="Jeep Wrangler", maxPassengers=5, maxSpeed=160)
xe_jeep.drive()
xe_jeep.soundHorn()