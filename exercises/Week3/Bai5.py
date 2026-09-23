# Viết chương trình với yêu cầu sau:
# - Định nghĩa một hàm với tên tinhGiaithua(). Hàm nhận vào một tham số n kiểu
# nguyên và thực hiện tính giai thừa của n, sau đó trả về giai thừa của n.
# - Viết mã để minh họa sử dụng hàm vừa định nghĩa ở trên.

def tinhGiaiThua(a):
    giaiThua=1
    for i in range(1,a+1):
        giaiThua*=i
    return giaiThua

a=int(input("Nhap vao so a: "))
print(tinhGiaiThua(a))