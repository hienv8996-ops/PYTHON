s = input("Nhập xâu: ")
so = 0
hoa = 0
thuong = 0
ki_tu = 0
for i in range(len(s)):
    if s[i].isdigit():
        so += 1
    elif s[i].isupper():
        hoa += 1
    elif s[i].islower():
        thuong += 1
    else:
        ki_tu += 1
print("Số lượng ký tự số:", so)
print("Số lượng chữ cái in hoa:", hoa)
print("Số lượng chữ cái thường:", thuong)
print("Số lượng ký tự đặc bệt:", ki_tu)