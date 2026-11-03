DSSV = []
Sosv=3
def nhapds(ds):
    for i in range(sosv):
        print("Nhap sinh vien thu", i + 1)
        masv = input("Nhap ma sinh vien: ")
        ten = input("Nhap ho ten: ")
        gioitinh = input("Nhap gioi tinh: ")
        toan = float(input("Nhap diem Toan: "))
        ly = float(input("Nhap diem Ly: "))
        hoa = float(input("Nhap diem Hoa: "))
        DTB = (toan + ly + hoa/ 3)
    if DTB >= 8:
        xeploai ="giỏi"
    elif DTB >=6.5:
        xeploai = "khá"
    elif DTB >=5:
        xeploai ="trung bình"
    else:
        xeploai =" yếu"
    sv={"MASV":masv, "Tên":ten, "Gioi tính":gioitinh,"Tuổi":tuoi,
        "Toán":toan,"Lý":ly, "Hóa":hoa, "DTB":DTB,"Xếp loại":xeploai}
    DSSV.append(sv)
def inds():
    print("danh sách sinh viên")
    for sv in DSSV:
        print( sv.get("MASV"),"-",sv.get("Tên"),"-", sv.get("Gioi tính"),"-",sv.get("Tuổi"),
        sv.get("Toán"),"-",sv.get("Lý"),"-", sv.get("Hóa"),"-",sv.get("DTB"),"-",sv.get("Xếp loại"))
def themsinhvien():
    print("nhập thông tin sinh viên cần thêm: ")
    masv = input("Nhap ma sinh vien: ")
    ten = input("Nhap ho ten: ")
    gioitinh = input("Nhap gioi tinh: ")
    toan = float(input("Nhap diem Toan: "))
    ly = float(input("Nhap diem Ly: "))
    hoa = float(input("Nhap diem Hoa: "))
    DTB = (toan + ly + hoa / 3)
if DTB >= 8:
    xeploai = "giỏi"
elif DTB >= 6.5:
    xeploai = "khá"
elif DTB >= 5:
    xeploai = "trung bình"
else:
    xeploai = " yếu"
sv = {"MASV": masv, "Tên": ten, "Gioi tính": gioitinh, "Tuổi": tuoi,
      "Toán": toan, "Lý": ly, "Hóa": hoa, "DTB": DTB, "Xếp loại": xeploai}
DSSV.append(sv)

sosv=int(input("số lượng sinh viên"))
nhapds()
inds()

