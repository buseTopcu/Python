#PANDAS SERİSİ OLUŞTURMAK

import numpy as np
import pandas as pd

#pandas serisi oluşturma
#numpy dan farklı olarak index değerlerini de saklar
seri = pd.Series([1,2,3,4,5,6,7,8,9])
seri

#serinin tipini görüntüleme
type(seri)

#serinin index bilgilerini erişme
#1 den 5 e kadar birer birer arttığını gösterdi
seri.axes

#serinin içindeki elemanların tipini sorgulama
seri.dtype 

#serinin eleman sayısını sorgulama
seri.size

#serinin boyutunu sorgulama. tek boyutlu array olarak değerlendiriyor
seri.ndim

#sadece serinin içindeki değerlere bir np.array gibi erişme
seri.values

#serinin ilk 5 elemanını listeleme
seri.head()

#arguman olarak istenilen değer sayuısı da girilebilir
seri.head(3)

#serinin son elemanlarını listeleme
seri.tail()

#son dört eleman
seri.tail(4)

#INDEX İSİMLENDİRME

pd.Series([99,88,77,66,55])

#index değerlerini değiştirme 
pd.Series([99,88,77,66,55], index = [1,3,5,7,9])

#string değerler ile indexi isimlendirme
seri = pd.Series([99,88,77,66,55], index = ["a","b","c","d","e"])
seri
seri["a"]
seri["a":"c"]


#SÖZLÜK ÜZERİNDEN LİSTE OLUŞTURMA

sozluk = {"reg" : 10, "log" : 11, "cart" : 12}
seri = pd.Series(sozluk)
seri

#sozluk = pd.Series({"reg" : 10, "log" : 11, "cart" : 12})
#sozluk

#İKİ SERİYİ BİRLEŞTİRME

pd.concat([seri, seri])


#ELEMAN İŞLEMLERİ

a = np.array([1,2,33,444,75])
seri = pd.Series(a)
seri
seri[0]
seri[0:3]

seri = pd.Series([2,33,444,55], index = ["reg","loj","cart","rft"]) 
seri

#serilerin indexlerine erişme
seri.index

#serideki keys değerleri getirecek
seri.keys

#veriler key value şeklinde listelenir
list(seri.items())

#serinin elemanlarına erişme
seri.values


#eleman sorgulama
#serinin içinde bir değerin olup olmadığını sorgulama. true-false değeri döndürür
"reg" in seri
"a" in seri

#fancy ile eleman sorgulama
seri["rft"]
seri[["rft", "reg"]]
 
#elemanın değerini yeniden atama işlemi ile değiştirme
seri["reg"] = 130
seri["reg"]
seri["reg":"cart"]


#PANDAS DATAFRAME OLUŞTURMA

l = [1,2,63,35,85]

#dataFrame oluşturup columns ile isimlendirme
pd.DataFrame(l, columns = ["degisken_ismi"])

m = np.arange(1,10).reshape((3,3))
m

#np üzerinden iki boyutlu pandas dataFrame oluşturma
pd.DataFrame(m, columns = ["var1","var2","var3"])

#dataFrame isimlendirme
df = pd.DataFrame(m, columns = ["var1","var2","var3"])
df.columns

#columns değerlerine farklı değerler atadım
df.columns = ("deg1", "deg2", "deg3")
df

#dataFrame özellikleri

#dataFrame tipini sorgulama
type(df)

#dataFrame index bilgisini ve index değerlerini sorgulama
df.axes

#dataFrame boyut sorgulama
df.shape

#dataFrame vektörel boyut sorgulama. 
#satır ve sütun bilgisi olduğu için 2 çıktısını verecek
df.ndim

#dataFrame eleman sayısını sorgulama
df.size

#dataFrame değerlerini sorgulama
#dataFrame olan veri yapısının içinden sadece değerleri çekip numpy arraye dönüştürür
df.values
type(df.values)

#dataFrame başından ve sonundan listeleme
df.head()
df.tail(1)


#ELEMAN İŞLEMLERİ

s1 = np.random.randint(10, size = 5)
s2 = np.random.randint(10, size = 5)
s3 = np.random.randint(10, size = 5)

#numpy arrayden sözlük oluşturma
sozluk = {"var1" : s1, "var2" : s2, "var3" : s3,}
sozluk

#sözlükten dataFrame oluşturma
df = pd.DataFrame(sozluk)
df

#0. indexten 2. indexe kadar listeleme
df[0:2]

#index değerlerini listeleme
df.index

#index değerlerini değiştirme
df.index = ["a","b","c","d","e"]
df

#index listeleme
df["c":"e"]


#SİLME İŞLEMİ

#drop fonksiyonu ile silme işlemi gerçekleştirilir.
#fakat silme işleminden sonra dataFrame tekrar görüntülendiğinde,
#aslında silme işleminin gerçekleşmediğini görebiliriz
df.drop("a")
df

#silme işleminin kalıcı olması için inplace argümanı kullanılır
df.drop("a", inplace = True)
df


#fancy

#verilen iki farklı değeri silme
l = ["c","e"]
df.drop(l, axis = 0)


#değişkenler için 

#değişkenin dataFrame içinde olup olmadığını sorgulama
"var1" in df

#for ile verilen listeledeki değerlerin olup olmadığını kontrol etme
l = ["var1","var2"]

for i in l:
    print(i in df)


#var1 ve var2 sütunlarının çarpımından var4 sütunu oluştu
df["var4"] = df["var1"] * df["var2"]
df


#değişken silme
df.drop("var4", axis = 1, inplace = True)

#liste ile verilen değişkenleri silme
#axis ifadesi satırı silmek için yön belirtiyor
df.drop(l, axis = 1)


#GÖZLEM VE DEĞİŞKEN SEÇİMİ

#değerleri 1 ile 30 arasında değişen ona üçlük bir dataFrame oluşturma
m = np.random.randint(1,30, size = (10,3))
df = pd.DataFrame(m, columns = ["var1","var2","var3"])
df

#loc: tanımlandığı şekliyle seçim yapmak için kullanılır
#girilen bitiş değeri dahildir
df.loc[0:3]

#iloc: klasik indexleme mantığıyla işlem yapar
#girilen bitiş değeri dahil değildir
#hem gözlem hem değişken seçimi için index bağımsız seçim yapmak üzere kullanılır.
df.iloc[0:3]

#loc ve iloc arasında değişken seçme farklılığı
df.loc[0:3, "var3"]
df.iloc[0:3]["var3"]


#KOŞULLU ELEMAN İŞLEMLERİ

#df içerisindeki var1 değişkeninin elemanlarından 15 den büyük olanları listeleme
#listeleme işleminde var1 de koşulu sağlayan elemanlar dışında 
#o satırda bulunan var2 ve var3 değerleri de sıralandı
df[df.var1 > 15]

#sadece var1 elemanlarını listelemek için ayrıca belirtmek gerekiyor
df[df.var1 > 15]["var1"]

#birden fazla koşul girme
df[(df.var1 > 15) & (df.var3 < 20)]

#birden fazla eleman ile listeleme
df[(df.var1 > 15) & (df.var3 < 20)][["var1","var2"]]
df.loc[(df.var1 > 15) & (df.var3 < 20),["var1","var2"]]


#BİRLEŞTİRME (JOIN) İŞLEMLERİ

m = np.random.randint(1,30, size = (6,3))
df1 = pd.DataFrame(m, columns = ["var1","var2","var3"])
df1

df2 = df1 + 99
df2

#concat ile iki dataFrame i birleştime
pd.concat([df1,df2])

#dataFrameler birleşince index değerleri birbirini takip etmedi
#ikinci dataFrame yine sıfırdan başladı
#ignore_index parametresi true olarak girildiğinde index değerleri sıralanmış bir şekilde listelenir
pd.concat([df1,df2], ignore_index = True)

df2.columns = ["var1","var2","deg1"] 
df2

pd.concat([df1,df2], ignore_index = True)
#deg1 değerleri ile var3 değerleri  her iki veri setinde de olmadığı için boş olarak listelendi

#join parametresi ile her iki veri setinde de olan (kesişim) verileri birleştirdi
pd.concat([df1,df2], ignore_index = True, join = "inner")


#herhangi bir değişkene göre birleştime işlemi 
#df1 e ya da df2 ye göre birleştirerek listeleme 
pd.concat([df1,df2], ignore_index = True, join_axes = [df1.columns])
pd.concat([df1,df2], ignore_index = True, join_axes = [df2.columns])


#=========================================================================


df1 = pd.DataFrame({"calisanlar" : ["Ali", "Veli", "Ayse", "Fatma"], 
                    "grup": ["Muhasebe", "Muhendislik", "Muhendislik", "IK"]})
df1

df2 = pd.DataFrame({"calisanlar" : ["Ayse", "Ali", "Veli", "Fatma"], 
                    "ilk_giris" : [2010,2009,2014,2019]})
df2

#merge fonksiyonu birleştirmelerin hangi değişkene göre yapılacağını kendisi anlıyor
pd.merge(df1,df2)

#merge fonksiyonunda hangi değişkene göre birleştirme yapacağını da belirtebiliriz
pd.merge(df1,df2, on = "calisanlar")


#çoktan teke birleştirme

df3 = pd.merge(df1,df2)
df3

df4 = pd.DataFrame({"grup" : ["Muhasebe", "Muhendislik", "IK"], 
                    "mudur" : ["Caner","Mustafa","Berkcan"]})
df4

pd.merge(df3,df4)


#çoktan çoka birleştirme

df5 = pd.DataFrame({"grup" : ["Muhasebe","Muhasebe","Muhendislik","Muhendislik", "IK","IK"], 
                    "yetenekler" : ["matematik","excel","kodlama","linux","excel","yonetim"]})
df5

#yeteneklerin çoğul olmasından dolayı yetenek sayısı kadar çalışan sayısını da çoğalttı
pd.merge(df1,df5)


#GRUPLAMA VE TOPLULAŞTIRMA (grouping & aggregation)


# =============================================================================
# Basit toplulaştırma fonksiyonları:
#     count() ------------ sayma 
#     first()
#     last()
#     mean() ------------ ortalama 
#     median() ---------- medyan 
#     min()   ----------- min değer
#     max()   ----------- max değer
#     std()   ---------- standart sapma
#     var()  ------------- varyans
#     sum()  ------------- toplama
# =============================================================================

import seaborn as sns

#seaborn kütüphanesi içerisinde bulunan planets veri setini çağırdık
df = sns.load_dataset("planets")
df

df.shape

#1035*6 lık büyük bir veri seti olduğu için sadece ilk 10 verisini aldım
df.head(10)

#bütün değişkenlere mean fonksiyonunu uygulandı
df.mean()

#sadece istenilen değere fonksiyon uygulama
df["mass"].mean()
df["mass"].count()
df["mass"].min()
df["mass"].max()
df["mass"].std()
df["mass"].var()


#describe fonksiyonu ile veri setindeki tüm değişkenleri,
#betimsel istatistikler anlamında ortaya konulabilir
df.describe()

#Veri setlerinin transpozunu almak
df.describe().T

#dropna fonksiyonu ile veri seti içindeki eksik gözlemleri silme
#eksik gözlemler silindiğinde değerlerin bazılarıda değişiklikler olduğu gözlemlenebilir
df.dropna().describe().T


#gruplama işlemleri

df = pd.DataFrame({"gruplar" : ["A","B","C","A","B","C"], "veri" : [10,11,52,23,43,55]}, 
                   columns = ["gruplar","veri"])
df

#groupby fonksiyonu ile gruplar değişkeninde bulunan aynı değerler gruplanır
#gruplama işleminden sonra bir işlem yapılması istenmediyse verileri yalnızda saklar
df.groupby("gruplar")

#mean fonksiyonu ile gruplanan değerlerin ortalaması alınabilir
df.groupby("gruplar").mean()

df.groupby("gruplar").sum()


df = sns.load_dataset("planets")
df.head()

#method değerine göre değerleri gruplayıp orbital_period değerlerinin ortalamasını aldı
df.groupby("method")["orbital_period"].mean()
 
df.groupby("method")["orbital_period"].describe()


#==========================================================


df = pd.DataFrame({"gruplar" : ["A","B","C","A","B","C"], 
                   "degisken1" : [10,23,33,22,11,99], 
                   "degisken2" : [100,253,333,262,111,969]}, 
                    columns = ["gruplar","degisken1","degisken2"])
df

df.groupby("gruplar") 

#AGGREGATE

#aggregate fonksiyonu ile veriler üzerinde istenilen birden fazla toplulaştırma fonksiyonu çalıştırılabilir
#min ve max fonksiyonları pandasın kendi içerinde bulunan fonksiyonlar  olduğu için
#direk ya da tırnak içerisinde yazılabilir
#fakat median bir numpy kütüphanesine bağlı olduğu için numpy üzerinden çağırılmalıdır
df.groupby("gruplar").aggregate(["min", np.median, max])


#değişkenler için farklı istatistikler uygulama
#sözlük yapısı ile istenilen değişkene istenilen istatistik fonksiyon uygulanabilir
df.groupby("gruplar").aggregate({"degisken1" : min, "degisken2" : max})


#FILTER

def filterFunc(x):
    return x["degisken1"].std() > 9

#filter fonksiyonu ile sıradan bir filtreleme değil de,
#oluşturduğum fonksiyon üzerinden bir filtreleme işlemi gerçekleştirdim
df.groupby("gruplar").filter(filterFunc)


#TRANSFORM
#veri setleri içindeki değişkenleri dönüştürme işlemi gerçekleştirilir

df
df.transform(lambda x: x-x.mean())
#df içerisinde gruplar değişkeni bölümü nümeric ifadeler içermediği için,
#gruplar üzerinde mean fonksiyonunu çalıştıramıyor 
#bunun için sadece degiskenleri listeledim
dfA = df.iloc[:,1:3]
dfA.transform(lambda x: x-x.mean())
dfA.transform(lambda x: (x-x.mean()) / x.std())


#APPLY

#apply fonksiyonu transform ve filter fonksiyonu gibi,
#dataFrame in değişkenlerinin üzerinde gezinme yeteneği olan ve 
#toplulaştırma işlemi yapmak için kullanılan bir fonksiyondur. 

df = pd.DataFrame({"degisken1" : [10,23,33,22,11,99], 
                   "degisken2" : [100,253,333,262,111,969]}, 
                    columns = ["degisken1","degisken2"])
df

df.apply(np.sum)
df.apply(np.mean)

df = pd.DataFrame({"gruplar" : ["A","B","C","A","B","C"], 
                   "degisken1" : [10,23,33,22,11,99], 
                   "degisken2" : [100,253,333,262,111,969]}, 
                    columns = ["gruplar","degisken1","degisken2"])

#grupları birleştirip, kendisi bir isimlendirme yaptı
#birleştirdiği gruplar üzerine sum metodunu uyguladı
df.groupby("gruplar").apply(np.sum)


#PİVOT TABLOLAR

#Bu tablolar veri setleri üzerinde bazı satır ve sütun işlemleri yaparak,
#veri setini amaca uygun hale getirmek için kullanılır.
#groupby ın çok boyutlu versiyonu olarak düşünülebilir

import seaborn as sns

#seaborn kütüphanesinden titanic isimli veri setini çektim
titanic =  sns.load_dataset('titanic')
titanic.head()

titanic.groupby("sex")["survived"].mean()

titanic.groupby(["sex","class"])["survived"].aggregate("mean")

#unstack ile hiyerarşik yapı daha düzenli hale gelir
titanic.groupby(["sex","class"])["survived"].aggregate("mean").unstack()


#pivot ile tablo

#odaklandındığımız değişken survived, index olarak cinsiyet ve cinsiyetin yanında class bilgilerini görüntülemek istiyoruz 
#index ifadesi satırlarda, columns sütünlarda gösterilir
titanic.pivot_table("survived", index = "sex", columns = "class")

#titanic veri setinin içerisinde girdiğimiz aralıklarara göre yaş grubunu age değişkenine atadık
age = pd.cut(titanic["age"], [0, 18, 90])
age.head(10)

#age değişkeninin içerisinde bulunan değerleri pivot table ile görüntüledik
#yaş değeri bizim tanımladığımız değer olduğu için ve dışarıdan alındığı için tırnak işareti ile kullanılmaz.
#cinsiyet değişkeni veri setinin içinde olduğu için tırnak işareti ile ekledik
titanic.pivot_table("survived", ["sex", age], "class")


#DIŞ KAYNAKLI VERİ OKUMA

#txt ve csv formundaki dosyaları read_csv fonksiyonu ile okunur
#read_csv fonksiyonu içerisine dosyanın uzantısını alır
#sep argumanı ile veriler daha okunur hale gelir
pd.read_csv("reading_data/ornekcsv.csv", sep = ";")


pd.read_csv("reading_data/duz_metin.txt")

#excel formundaki dosyaları read_excel fonksiyonu ile okunur
df = pd.read_excel("reading_data/ornekx.xlsx")
df.head()

df.columns = ("A","B","C")
df.head()


tips = pd.read_csv("reading_data/tips.txt", sep = "\t")
tips.head(10)

