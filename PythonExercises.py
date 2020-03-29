def harf_say(x):
    return len(x)
 
harf_say("Merhaba!")

########################################

if [1,2,3,4][3] == 2:
    print("YES".lower())
else:
    print("NO") 
    
########################################

def islem(x,y):
    A = [x,y]
    return A[0] + A[1]

islem(1,3)

########################################

A = []
B = []

for i in [1,"a",12,"b"]:
    if type(i) == int:
        B.append(i)
    else:
        A.append(i)

A[1]

########################################

a=[10,20,30]
for i in a:
    print(i**2)
    
def islem(x, y):
    print(x - y)

islem(3)

########################################

import numpy as np

a = np.array([1,1,1])
b = np.array([2])

print(a+b)

########################################


A = [[1,2],[3,4],[5,6]]
print(list(map(lambda x: x[0]*3, A)))

########################################

A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A,B]
print(AB)

for i in AB:
    if type(i[0]) == int:
        print(list(map(lambda x: x-3, i)))


########################################


from functools import reduce
reduce(lambda a,b: a+b, ["a","4","a"])

########################################

list(filter(lambda x: x < 2, [1,2,3,4,5]))

########################################

a = [1,2,3]
list(map(lambda x: x*2, a))

########################################


from functools import reduce
A = ["Veri","Bilimi","Okulu"]
reduce(lambda a,b: a+b, list(map(lambda x: x[0], A)))

########################################

liste = ["a",20,10,30,"b"]
list(filter(lambda x: type(x) == int, liste))

########################################


A = []
for i in ["ali","veli","isik"]:
    A.append(i.replace("i","a"))
print(A)

########################################

from functools import reduce
a = [1,2,3,4]
reduce(lambda a,b: a*b, a)

########################################


list(map(lambda x: x/10, filter(lambda x: x > 20, [10,20,30,40,50])))

########################################

list(filter(lambda x: len(x) > 8, ["pazartesi","sali","carsamba","persembe","cuma"]))

########################################


list(map(lambda x: x.upper(), ["Ali","Veli","isik"]))

########################################


A = [1,2,3,4,5]

if type(A) == ():
    print("islem gecersiz")
else:
    print(list(map(lambda x: x/1, A)))

########################################


class VeriBilimci():
    calisanlar=[]
    diller=[]
    def __init__(self):
        self.bildigi_diller=[]
        self.bolum=""
    def dil_ekle(self,yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        VeriBilimci.diller.append(yeni_dil)

ali=VeriBilimci()
veli=VeriBilimci()

ali.bildigi_diller
ali.dil_ekle("R")
ali.bildigi_diller

veli.bildigi_diller
veli.dil_ekle("Python")
veli.bildigi_diller

VeriBilimci.diller











