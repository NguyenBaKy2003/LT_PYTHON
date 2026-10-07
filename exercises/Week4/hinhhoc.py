import math


def dien_tich_hinh_chu_nhat(dai, rong):
    return dai * rong


def dien_tich_hinh_tron(r):
    return math.pi * r ** 2


def dien_tich_hinh_thang(day_lon, day_nho, chieu_cao):
    return (day_lon + day_nho) * chieu_cao / 2


def dien_tich_tam_giac_vuong(canh_goc_vuong_1, canh_goc_vuong_2):
    return canh_goc_vuong_1 * canh_goc_vuong_2 / 2


def dien_tich_hinh_thoi(d1, d2):
    return d1 * d2 / 2


def dien_tich_tam_giac_can(day, chieu_cao):
    return day * chieu_cao / 2


def dien_tich_hinh_binh_hanh(day, chieu_cao):
    return day * chieu_cao