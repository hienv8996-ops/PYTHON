import math
n=int(input("nhập các giá trị dương và âm: \n"))
A=[]
for i in range(n):
    print(f"nhập phần tử thứ {i+1}: ",end='')
    x=float(input())
    A.append(x)
print(A)
danhsach_duong=[]
danhsach_am=[]
danhsach_0=[]

dem_duong = 0
dem_am = 0
dem_0 = 0

tong_duong = 0
tong_am = 0
for x in A:
    if x > 0:
        danhsach_duong.append(x)
        dem_duong += 1
        tong_duong += x
    elif x < 0:
        danhsach_am.append(x)
        dem_am += 1
        tong_am += -x
    else:
        danhsach_0.append(x)
        dem_0 += 1
print("Danh sách dương:", danhsach_duong)
print("Danh sách âm:", danhsach_am)
print("Danh sách 0:", danhsach_0)
print("Số lượng số dương:", dem_duong)
print("Số lượng số âm:", dem_am)
print("Số lượng số 0:", dem_0)
print("Tổng số dương:", tong_duong)
print("Tổng giá trị tuyệt đối của số âm:", tong_am)