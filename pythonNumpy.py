#numpy kütüphanesini import ettik
import numpy as np

#np array oluşturma
np.array([3,4,2,13])

#array içerisinde float bir değişken varsa diğer bütün değişkenleri floata çevirir
np.array([3.14,4,2,13])

#dtype isimli argüman ile sayı tipini kendimiz oluşturabiliriz
np.array([3.14,4,2,13], dtype="int")

###############################

#sıfırlardan oluşan array oluşturma
np.zeros(10, dtype=int)

#birlerden oluşan array oluşturma
np.ones((3,5), dtype=int)

#üçe beşlik üçlerden oluşan bir array oluşturma
np.full((3,5), 3)
 
#0 dan 31 e kadar 3 er 3 er artan bir sizi oluşturma
np.arange(0,31,3)

#0 ile 1 arasında 10 tane değer oluşturma
np.linspace(0,1,10)

#ortalaması 10 standart sapması 4 olacak 3 e 4 lük bir array oluşturma
np.random.normal(10, 4, (3,4))

#rastgele integer sayılardan oluşan 3 e 3 lük bir matris oluşturma
np.random.randint(0,10, (3,3))

#NUMPY ARRAY ÖZELLİKLERİ

#0 dan 10 a kadar 10 adet rastgele int sayı oluşturma
a = np.random.randint(10, size=10)

#arrayin boyut sayısını verir
a.ndim

#arrayin boyut bilgisini verir
a.shape

#arrayin eleman sayısını verir
a.size

#arrayin tip bilgisini verir
a.dtype

b = np.random.randint(10, size = (3,5))
b
b.ndim
b.shape
b.size
b.dtype

#YENİDEN ŞEKİLLENDİRME (RESHAPING)

np.arange(1,10)

#oluşturulmuş tek boyutlu bir arrayi matrise dönüştürme 
np.arange(1,10).reshape((3,3))

a = np.arange(1,10)

#b bir vektörün taşıdığı değerleri taşır fakat 1 satır 9 sütundan oluşur
b = a.reshape((1,9))
b.ndim

#ARRAY BİRLEŞTİRME (Concantenation)

x = np.array([1,2,3])
y = np.array([4,5,6])

np.concatenate([x,y])

z = np.array([7,8,9])
np.concatenate([x,y,z])

#iki boyutlu

a = np.array([[1,2,3], [4,5,6]])
a
np.concatenate([a,a])
#axis in ön tanımlı değeri 0 olduğu için satır bazında birleştirdi

#axis değeri 1 olarak girilirse sütun bazlı birleştirir
np.concatenate([a,a], axis = 1)

#ARRAY AYIRMA (Splitting)

x = np.array([1,2,3,99,99,3,2,1])

#arrayi 3 den ve 5 den ayır
np.split(x, [3,5])

#oluşan arrayleri sırayla verilen değişkenlere atayacak
a,b,c = np.split(x, [3,5])
a
b
c

#iki boyutlu ayırma

m = np.arange(16).reshape(4,4)
m

#arrayi 2 den böl
np.vsplit(m, [2])

ust,alt = np.vsplit(m, [2])
ust
alt

#dikey bölme işlemi 
np.hsplit(m, [2])

sag,sol = np.hsplit(m, [2])
sag
sol


#SIRALAMA (sorting)

v = np.array([1,6,8,2,3,5,1,2])


np.sort(v)
v
#sıralama işlemi sonucunda verinin orjinal sırasını bozmadı

v.sort()
v
#sıralama işlemi sonucunda verinin orjinal sırasını bozdu

#iki boyutlu

m = np.random.normal(20,5, (3,3))
m

#herbir satırı küçükten büyüğe sıraladı
np.sort(m, axis = 1)

#herbir sütunu küçükten büyüğe sıraladı
np.sort(m, axis = 0)


#INDEX İLE ELEMANLARA ERİŞMEK

a = np.random.randint(10, size = 10)
a

#birinci elemana erişme
a[0]

#sondan biinci elemana erişme
a[-1]

#sıfırıncı indexteki elemanı değiştirme 
a[0] = 100
a

#iki boyutlu

m = np.random.randint(10, size = (3,5))
m

#sıfırıncı satır sıfırıncı sütuna erişme
m[0,0]

#birinci satır dördüncü sütuna erişme
m[1,4]

#birinci satır dördüncü sütundaki değeri değiştirme
m[1,4] = 22
m

#int arraya float sayı ekleme
m[1,4] = 2.2
m
#sayıyı ondalık kısmını keserek ekledi

#SLICING İLE ELEMANLARA ERİŞMEK

a =np.arange(20,30)
a

#0. indexten dan 3 e kadar olan sayıları listele. 3 dahil değil
#başlangıç indexi belirtilmezse 0 dan itibaren alır.
a[0:3]
a[:3]

#2. indexten 5. indexe kadar olan sayıları listeleme
a[2:5]

#3. indexten arrayin sonuna kodar listeleme 
a[3:]

#ilk elemandan başlayarak arrayin sonuna kadar ikişer ikişer listeleme
a[1::2]
a[0::3]


#iki boyutlu

m = np.random.randint(10, size = (5,5))
m

#":" ile bütün satıları seçti ve 0. sütunü seçti. 0. sütunu seçmiş oldu
#sütun bazlı işlem
m[:,0]
m[:,4]

#0. satır ve tüm sütunları listeleme. ilk satırı seçme
m[0,:]

#birinci satırı seçme
m[1,:]  

#0 dan 2 ye kadar satırları, 0 dan 3 e kadar sütunları alma
m[0:2 , 0:3]

#ilk iki sütunu alma
m[:,:2]


#ALT KÜME ÜZERİNDE İŞLEM YAPMA

m = np.random.randint(10, size = (5,5))
m

alt_a = a[0:3, 0:2]
alt_a[0,0] = 999
alt_a[1,1] = 888
alt_a
m

#alt kümede işlem yapılmasına rağmen orjinal array de değişime uğradı
#orjinal arrayin değişmesi istenmiyorsa copy kullanılır
#copy metodu ile ana arrayden bağımsız oluşturulabilir
alt_b = m[0:3, 0:2].copy()
alt_b
alt_b[0,0] = 999
alt_b
m

#FANCY INDEX İLE ELEMANLARA ERİŞMEK

v = np.arange(0,30,3)
v

#v arrayinin içerisinde bulunan 1. 3. ve 5. index elemanlarını getirdi
getir = [1,3,5]
v[getir]

#iki boyutta

m = np.arange(9).reshape((3,3))
m = np.arange(0,10,2)
m

satir = np.array([0,1])
satir
sutun = np.array([1,2])
sutun
m[satir, sutun]

#basit index ile fancy index/slice
m[0, [1,2]]
m[0:, [1,2]]


#KOŞULLU ELEMAN İŞLEMLERİ

v = np.array([1, 2, 3, 4, 5])

#array içinde dolaşıp her elemanın 5 den küçük olup olmadığını sorgular
#true-false değerleri döndürür
v < 5
v > 3

#arrayin içinde verilen koşulu sağlayan değerleri yazdırdı
v[v > 3]
v[v < 3]
v[v <= 3]
v[v == 3]
v[v != 3]


#MATEMATİKSEL İŞLEMLER

v = np.array([1, 2, 3, 4, 5])

v - 1
v + 5                      
v * 5                       
v / 5                      
v ** 3                    
v * 5 / 10 - 1
v % 2                     


#ufunc

v - 1                      # = np.subtract(v, 1)
v + 5                      # = np.add(v, 5)
v * 5                      # = np.multiply(v, 5)  
v / 5                      # = np.divide(v, 5)
v ** 3                     # = np.power(v, 3)
v % 2                      # = np.mod(v, 2)

#mutlak değer
np.absolute(np.array([-3]))

np.sin(360)
np.cos(180)

#verilen arrayin içindeki elemanların logaritmasını alır.
#istenilen tabanda yazdırılabilir
np.log(v)
np.log2(v)
np.log10(v) 


#İSTATİSTİKSEL HESAPLAMALAR

v
v.mean()
v.sum()
v.min()
v.max()
v.var()
v.std()
v.corrcoef()


#İKİ BİLİNMEYENLİ DENKLEM ÇÖZÜMÜ (linalg kütüphanesi)

#5 * x0 + x1 = 12
#x0 + 3 * x1 =10

#x0 ve x1 değerlerinin katsayıları
a = np.array([[5,1], [1,3]])
#denkelemin sonuçları
b = np.array([12, 10])

x = np.linalg.solve(a, b)
x
