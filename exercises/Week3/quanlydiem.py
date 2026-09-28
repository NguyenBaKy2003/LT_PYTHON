
def lap_trinh_co_so(chuyen_can, qua_trinh, cuoi_ky):
    return chuyen_can * 0.1 + qua_trinh * 0.3 + cuoi_ky * 0.6


def tieng_anh(chuyen_can, qua_trinh, cuoi_ky):
    return chuyen_can * 0.1 + qua_trinh * 0.3 + cuoi_ky * 0.6


def phan_tich_du_lieu(chuyen_can, qua_trinh, cuoi_ky):
    return chuyen_can * 0.1 + qua_trinh * 0.3 + cuoi_ky * 0.6


def xeploai(diem_lap_trinh, diem_tieng_anh, diem_phan_tich):
    diem_trung_binh = (
        diem_lap_trinh +
        diem_tieng_anh +
        diem_phan_tich
    ) / 3

    if diem_trung_binh >= 8.5:
        xep_loai = "Giỏi"
    elif diem_trung_binh >= 7.0:
        xep_loai = "Khá"
    elif diem_trung_binh >= 5.0:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"

    return diem_trung_binh, xep_loai