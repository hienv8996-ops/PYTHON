def UCLN(so1,so2):
    while so1 !=so2:
        if so1 > so2:
            so1 -= so2
        else:
            so2 -= so1
    return so1
def rutgon(tu,mau):
    tu1 = tu
    tu = tu /UCLN(tu,mau)
    mau = mau/UCLN(tu,mau)
    print(tu,"/",mau)
def cong(tu1,mau1,tu2,mau2):
    tu = tu1*mau2 + tu2*mau1
    mau = mau1*mau2
    rutgon(tu,mau)
def tru(tu1,mau1,tu2,mau2):
    tu = tu1*mau2 - tu2*mau1
    mau = mau1*mau2
    rutgon(tu,mau)
def nhan(tu1,mau1,tu2,mau2):
    tu = tu1*tu2
    mau = mau1*mau2
    rutgon(tu,mau)
def chia(tu1,mau1,tu2,mau2):
    tu = tu1*mau2
    mau = mau1*tu2
    rutgon(tu,mau)
cong(1,2,5,6)

