nam = int(input('nhập năm bất kì: '))
if (nam%4==0 and nam%100!=0) or (nam%400==0):
    print(nam,'la nam nhuan')
else:
    print(nam,'không là năm nhuận')