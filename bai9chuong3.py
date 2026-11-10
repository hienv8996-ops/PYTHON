DSSV = []
def nhapds(ds):
    sosv = int(input("số lượng sinh viên"))
    for i in range(sosv):
        print("Nhap sinh vien thu", i + 1)
        masv = input("Nhap ma sinh vien: ")
        ten = input("Nhap ho ten: ")
        gioitinh = input("Nhap gioi tinh: ")
        tuoi=int(input("Tuổi: "))
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
    tuoi = int(input("Tuổi: "))
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

def catnhapsinhvien(masv):
    for sv in DSSV:
        if sv["MASV"]==masv:
            ten = input("nhập tên:")
            gioitinh = input("Nhap gioi tinh: ")
            tuoi = int(input("Tuổi: "))
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
            sv["Tên"]=ten
            sv["Gioitinh"]=gioitinh
            sv["Tuoi"]=tuoi
            sv["Toan"]=toan
            sv["Ly"]=ly
            sv["Hoa"]=hoa
            sv["Dtb"]=Dtb
            sv["Xeploai"]=xeploai

def xoasinhvien(masvxoa):
    for sv in DSSV:
        if sv["MASV"]==masvXoa:
            DSSV.remove(sv)

def timkiem(tencantim):
    for sv in DSSV:
        if sv["MASV"] == tencantim:
            return "có sinh viên cần tìm"
        return "không có sinh viên cần tìm"

def Demsv(tencantim):
    for sv in DSSV:
        if sv["MASV"] == tencantim:
            dem+=1
        return dem

def sapxeptheodtb():
    return sorted(DSSV,key=lambax:x["DTB"])
def sapxeptheoTen():
    return sorted(DSSV,key=lambax:x["Tên"])
def sapxeptheoMa():
    return sorted(DSSV,key=lambax:x["Mã"]))



nhapds(DSSV)
inds()

themsinhvien()
print("danh sách sv sau khi sửa: ")
inds()

Masvcansua=input("nhập mã sinh viên cần sửa: ")
catnhapsinhvien(masv)
print("Danh sách sinh viên sau khi sửa: ")
inds()

masvxoa = input("nhập mã sinh viên xóa: ")
xoasinhvien(masvxoa)

tencantim=input("nhập sinh viên cần tìm: ")
print(timkiem(tencantim))
print(Demsv(tencantim))

print("danh sách sinh viên sắp xếp theo Dtb: ")

