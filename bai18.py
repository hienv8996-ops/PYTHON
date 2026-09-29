import math
n =int(input('nhập n: '))
dem = 0
for a in range (2,n):
    kt = True
for i in range(2, int(math.sqrt(a))*1):
    if a%i==0:
        kt= False
        break
        dem += 1
if kt==True:
    dem+=1
print('có',dem,'số nguyên tố nhỏ hơn',n)


