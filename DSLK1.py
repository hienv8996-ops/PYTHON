class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class DSLK:
    def  __init__(self):
        self.head=None
    def themdau(self,data):
        new_node=Node(data)
        new_node.next =self.head
        self.head=new_node
    def inds(self):
        p = self.head
        while p is not None:
            print(p.data,end='->')
            p=p.next
        print('None')
    def themcuoi(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=new_node
    def chiahetcho2(self):
        if self.head is None:
            return
        print("danh sách các số Chiahetcho2")
        p=self.head
        tong = 0
        while p.next is not None:
            if p.data %2==0:
                print(p.data,end='->')
                tong=tong+p.data
            p=p.next
        print("Tổng là: ",tong)
    def Timkiem(self,x):

        if self.head is None:
                return
        p =self.head
        while p is not None:
            if p.data ==x:
                return p
            p=p.next
        return None
ds=DSLK()
ds.themdau(3)
ds.themdau(9)
ds.themdau(5)
ds.themcuoi(10)
ds.inds()
ds1=DSLK()
ds1.themdau(8)
ds1.themdau(6)
ds1.themcuoi(10)
ds1.inds()
ds2=DSLK()
n=10
for i in range (n):
    ds2.themdau(i + 1)
n=20
for i in range(n):
    if i % 3==0:
        ds2.themcuoi(i)
ds2.inds()
ds2.chiahetcho2()

x = int(input("nhập giá trị cần tìm: "))
kq=ds2.Timkiem(x)
if kq is not None:
    print(f"tìm thấy giá trị{x} trong ds2")
else:
    print(f"không tìm thấy {x} trong ds2")



