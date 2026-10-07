n=int(input("nhập số phân tử của dãy: "))
A=[]
for i in range(n):
    print(f"nhập phần tử thứ {i+1}: ",end='')
    x=float(input())
    A.append(x)
print(A)
so_sv_dat=0
so_sv_truot=0
B=[]
max=A[0]
vitri_max=0
for i in range(n):
    if A[i]>=5:
        so_sv_dat=so_sv_dat+1
    else:
        so_sv_truot=so_sv_truot+1
    if A[i]>=7:
        B.append(A[i])
    if A[i]>max:
        max=A[i]
        vitri_max=i
print("số sinh viên đạt", so_sv_dat)
print("số sinh viên trượt",so_sv_truot)
print("danh sách số sinh viên có điểm>=7",B)
print(f"điểm lớn nhất {max}  tại vị trí {vitri_max}")