import math


def giai_thua(n):
    if n < 0:
        return None

    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i

    return ket_qua


def tong(a, b):
    return a + b


def hieu(a, b):
    return a - b


def tich(a, b):
    return a * b


def thuong(a, b):
    if b == 0:
        return None
    return a / b


def dien_tich_hinh_tru(r, h):
    return 2 * math.pi * r * (r + h)


def dien_tich_hinh_vuong(a):
    return a * a


def lap_phuong(n):
    return n ** 3