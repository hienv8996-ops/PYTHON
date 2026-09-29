chuoi =input("nhập chuỗi: ")
chuoichuanhoa=""
kt = True
while kt:
    vt = chuoi.find(" ")
    if vt ==-1:
        kt = False
        break
    else:
        tu = chuoi[0:vt:1]
        print(tu)
        chuoichuanhoa+=tu+""
        chuoi = chuoi[vt+1:len(chuoi):1].strip()
print(chuoi.title())
chuoichuanhoa=chuoi.title()
print("chuỗi đã chuẩn hóa: ",chuoichuanhoa.split())
