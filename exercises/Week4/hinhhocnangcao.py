import math


def chu_vi_hinh_binh_hanh(a, b):
    return 2 * (a + b)


def dien_tich_hinh_binh_hanh(day, chieu_cao):
    return day * chieu_cao



def chu_vi_hinh_tru(r, h):
    return 2 * math.pi * r


def dien_tich_hinh_tru(r, h):
    return 2 * math.pi * r * (r + h)



def chu_vi_hinh_thoi(canh):
    return 4 * canh


def dien_tich_hinh_thoi(d1, d2):
    return (d1 * d2) / 2




def chu_vi_hinh_ngu_giac_deu(canh):
    return 5 * canh


def dien_tich_hinh_ngu_giac_deu(canh):
    return (1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * canh ** 2




def chu_vi_hinh_thang_can(a, b, c):

    return a + b + 2 * c


def dien_tich_hinh_thang_can(a, b, h):
    return (a + b) * h / 2