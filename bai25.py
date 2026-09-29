n = int(input("Nhập số nguyên: "))
tong = 0
while n > 0:
    so = n % 10
    tong += so
    n = n // 10
print("Tổng các chữ số là:", tong)
