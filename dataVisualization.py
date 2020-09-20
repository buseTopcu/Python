"""
@author: Buse TOPCU
"""

#OBJECT-KATEGORÄ°K DÃ–NÃœÅžTÃœRME

import seaborn as sb
import pandas as pd

planets = sb.load_dataset("planets")
planets.head()

# copy metodu ile veri seti Ã¼zerinde iÅŸlem yapmadan veri seti ilk haliyle saklanabilir
df = planets.copy()

# method deÄŸiÅŸkeninin tÃ¼rÃ¼ object olarak gÃ¶rÃ¼ntÃ¼leniyor
# object kategorik bir deÄŸiÅŸkendir
# bazÄ± Ã§alÄ±ÅŸmalarda analitik yaklaÅŸÄ±mlara ve bazÄ± fonksiyonlara en uygun format kategoriktir
# bu nedenle object i kategorik formata dÃ¶nÃ¼ÅŸtÃ¼rmek gerekiyo
df.info()
df.dtypes

# Categorical metodu ile method deÄŸiÅŸkeninin tipini deÄŸiÅŸtirilir
df.method = pd.Categorical(df.method)
df.dtypes

# deÄŸiÅŸken ve gÃ¶zlem sayÄ±sÄ±na eriÅŸmek
df.shape

# deÄŸiÅŸken isimlerine eriÅŸmek
# describe metodu eksik gÃ¶zlemleri gÃ¶z ardÄ± eder ve kategorik deÄŸiÅŸkenleri dÄ±ÅŸarÄ±da tutar
df.columns
df.describe().T

#include=all ile bÃ¼tÃ¼n deÄŸiÅŸkenleri iÃ§ermesi saÄŸlanabilir
df.describe(include="all").T

#------------------------------------------------------------------------

#EKSÄ°K DEÄžERLERÄ°N Ä°NCELENMESÄ°


df = planets.copy()
planets.head()

# deÄŸiÅŸkenlerin herhangi birinde eksik gÃ¶zlem olup olmadÄ±ÄŸÄ±nÄ± sorgulama
df.isnull().values.any()

# hangi deÄŸiÅŸkenlerde toplam kaÃ§ tane eksik gÃ¶zlem olduÄŸunu sorgulama
df.isnull().sum()

# eksik gozlemler sorun Ã§Ä±karmasÄ±n diye eksik deÄŸerlerin yerine
# ortalama deÄŸeri ya da direk sÄ±fÄ±r deÄŸeri yazÄ±labilir
df["orbital_period"].fillna(0, inplace=True)
df.isnull().sum()

#eksik gÃ¶zlemler yerine ortalama deÄŸer koyma
#df["orbital_period"].fillna(df.orbital_period.mean(), inplace=True)

#veri setindeki tÃ¼m deÄŸelere ortalama deÄŸeri atama
#df.fillna(df.mean(), inplace=True)


#--------------------------------------------------------------

#KATEGORÄ°K DEÄžÄ°ÅžKENLER

df = planets.copy()
planets.head()

#dataframe iÃ§inden istediÄŸimiz tipe gÃ¶re deÄŸiÅŸken seÃ§mek iÃ§in kullanÄ±lÄ±r
#object kategorik olarak deÄŸiÅŸtirildiyse object yerine kategorik yazÄ±lmalÄ±dÄ±r
kat_df = df.select_dtypes(include=["object"])
kat_df.head()

#deÄŸiÅŸkenin iÃ§indeki bÃ¼tÃ¼n sÄ±nÄ±f bilgilerine eriÅŸme
kat_df.method.unique()

#deÄŸiÅŸkenin iÃ§indeki bÃ¼tÃ¼n sÄ±nÄ±flarÄ±n isimleri
kat_df["method"].value_counts().count()

#kategorik deÄŸiÅŸkenin sÄ±nÄ±flarÄ±nÄ±n sayÄ±sÄ±na eriÅŸme
kat_df["method"].value_counts()

#kategorik deÄŸiÅŸkenlerin sayÄ±sÄ±nÄ± barh(sÃ¼tun grafiÄŸi) ile gÃ¶rselleÅŸtirdim
#kodun sonuna noktalÄ± virgÃ¼l konulursa grafikten Ã¶nce yazÄ±lan bilgi mesajÄ± yazÄ±lmaz 
df["method"].value_counts().plot.barh()
df["method"].value_counts().plot.barh();


#------------------------------------------------------------------------

# SUREKLI DEGISKENLER

df = planets.copy()
planets.head()

df_num =df.select_dtypes(include=["float64", "int64"])
df_num.head()
df_num.describe().T

#belirli bir degerlerin betimsel istatistiklerine erisme
df_num["distance"].describe()

("Ortalam: " + str(df_num["distance"].mean()))
("Dolu gozlem sayisi: " + str(df_num["distance"].count()))
("Max deger: " + str(df_num["distance"].max()))
("Min deger: " + str(df_num["distance"].min()))
("Medyan: " + str(df_num["distance"].median()))
("Standart Sapma: " + str(df_num["distance"].std()))


#------------------------------------------------------------------------

#DAGILIM GRAFIKLERI

diamonds = sb.load_dataset("diamonds")
df = diamonds.copy()
df.head()

df.info()

df.describe().T

df["cut"].value_counts()
df["color"].value_counts()

#ordinal tanımlama

from pandas.api.types import CategoricalDtype

#cut degerini kategorik değiskene donusturur ve sıralamayı(ordinal) bir sekilde yapar
df.cut = df.cut.astype(CategoricalDtype(ordered = True))

#cut degerinin kategorik degisken olarak degerlerini gozlemledim
df.dtypes

#kendi icerisinde kalite degerlerini sıraladı
df.cut.head(1)

# fakat bu kategorik degisken dogru bir sıralama yapmadı
# doÄŸru sıralama: (Fair > Good > Very Good > Premium > Ideal)
# kendi kategorileri sıralamamızı yazmamız daha iyi olacaktır
cut_kategoriler = ["Fair", "Good", "Very Good", "Premium", "Ideal"]

#categories ile kategorisi belirtilir
df.cut = df.cut.astype(CategoricalDtype(categories = cut_kategoriler, ordered = True))

#kategori sÄ±rasÄ± deÄŸiÅŸti
df.cut.head(1)



#BARPLOT - KATEGORÄ°K DEÄžÄ°ÅžKENLER Ä°Ã‡Ä°N

# sÃ¼tun grafikleri kategorik deÄŸiÅŸkenleri gÃ¶rselleÅŸtirmek iÃ§in kullanÄ±lÄ±r

df["cut"].value_counts().plot.barh();

#set_title ile grafiÄŸe baÅŸlÄ±k eklenebilir
df["cut"].value_counts().plot.barh().set_title("Cut DeÄŸiÅŸkeninin SÄ±nÄ±f FrekanslarÄ±");

#seaborn gÃ¶rselleÅŸtirmesi

#x eksenine cut deÄŸiÅŸkenini y eksenine cut indexlerini koyup grafik oluÅŸturduk
sb.barplot(x = "cut", y = df.cut.index, data = df);


#Ã‡APRAZLAMALAR

#Ã‡aprazlama veri seti iÃ§erisindeki deÄŸiÅŸkenlerin birlikte deÄŸerlendirilmesidir


#from pandas.api.types import CategoricalDtype
#diamonds = sb.load_dataset("diamonds")
#df = diamonds.copy()
#cut_kategoriler = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
#df.cut = df.cut.astype(CategoricalDtype(categories = cut_kategoriler, ordered = True))
#df.head()

sb.catplot(x = "cut", y = "price", data = df);

#hue ile ucuncu boyut eklenebilir
sb.barplot(x = "cut", y = "price", hue = "color", data = df);

df.groupby(["cut","color"])["price"].mean()


#------------------------------------------------------------------------

#Histogram ve YoÄŸunluk GrafiÄŸinin OluÅŸturulmasÄ± - SAYISAL DEÄžÄ°ÅžKENLER Ä°Ã‡Ä°N

#kde argumanÄ± yoÄŸunluk fonksiyonunun grafiÄŸin Ã¼zerine konulup konulmamasÄ± iÃ§in kullanÄ±lÄ±r
sb.distplot(df.price, kde = False);

#bins argumanÄ± histogram Ã¼zerindeki hassasiyeti temsil eder
sb.distplot(df.price, bins = 1000, kde = False);

#sadece yoÄŸunluk grafiÄŸi Ã§izme
sb.distplot(df.price, hist = False);

#shade = True histogramın altında kalan kısım doldurulur
sb.kdeplot(df.price, shade = True)

#Ã§aprazlamalar

#FacetGrid grafik Ã¼zerine eklenen boyutlarÄ± bÃ¶lerek gÃ¶stermek iÃ§in kullanÄ±lÄ±r
#hue ile boyut eklenir
#xlim ile x ekseninde verilen deÄŸerler arasÄ±nda sÄ±nÄ±rlandÄ±rÄ±lmÄ±ÅŸ veri gÃ¶sterilir
#add_legend deÄŸiÅŸkenin kategorik bilgileri eklenir
sb.FacetGrid(df, hue = "cut", height = 5, xlim = (0, 10000)).map(sb.kdeplot, "price", shade = True).add_legend();

sb.catplot(x = "cut", y = "price", hue = "color", kind = "point", data = df);

#------------------------------------------------------------------------

#BOXPLOT - SAYISAL DEÄžÄ°ÅžKENLER Ä°Ã‡Ä°N - DAÄžILIM GRAFÄ°KLERÄ°

#tips veri seti hikayesi
#total_bill: yemeÄŸin toplam fiyatÄ± - bahÅŸiÅŸ ve vergi dahil
#tip
#sex: Ã¼creti Ã¶deyen kiÅŸinin cinsiyeti - 0=male, 1=female
#smoker: grupta sigara iÃ§en var mÄ± - 0=no, 1=yes
#day(3=Thur, 4=Fri, 5=Sat, 6=Sun)
#time - 0=day, 1=night
#size


tips = sb.load_dataset("tips")
daf = tips.copy()
daf.head()


#verilerin iÃ§eriklerinin gÃ¶zlemlenmesi
daf["sex"].value_counts()

daf["smoker"].value_counts()

daf["day"].value_counts()

daf["time"].value_counts()


sb.boxplot(x = daf["total_bill"]);
sb.boxplot(x = daf["total_bill"], orient = "v");


#hangi gÃ¼nler ne kadar para kazanÄ±lmÄ±ÅŸ
sb.boxplot(x = "day", y = "total_bill", data = daf);
#Pazar gÃ¼nÃ¼ cumartesi gÃ¼nÃ¼nden daha az mÃ¼ÅŸteri gelmesine raÄŸmen kazanÃ§ daha fazla

#sabah mÄ± akÅŸam mÄ± daha fazla para kazanÄ±lÄ±yor
sb.boxplot(x = "time", y = "total_bill", data = daf);
#akÅŸam yemeklerinde daha fazla para kazanÄ±lmÄ±ÅŸ

#yemeÄŸe gelen kiÅŸi sayÄ±sÄ± ile kazanÃ§ arasÄ±ndaki baÄŸlantÄ±
sb.boxplot(x = "size", y = "total_bill", data = daf);


sb.boxplot(x = "size", y = "total_bill", hue = "sex", data = daf);
#sadece cumartesi gÃ¼nÃ¼ kadÄ±nlar daha fazla hesap Ã¶demiÅŸ


#------------------------------------------------------------------------

#VIOLIN Grafikleri - SAYISAL DEÄžÄ°ÅžKENLER Ä°Ã‡Ä°N - DAÄžILIM GRAFÄ°KLERÄ°

sb.catplot(y = "total_bill", kind = "violin", data = daf);

#Ã‡aprazlama
sb.catplot(x= "day", y = "total_bill", kind = "violin", data = daf);

sb.catplot(x= "day", y = "total_bill", hue = "sex", kind = "violin", data = daf);

#------------------------------------------------------------------------
########################################################################


#KORELASYON Grafikleri
#Ä°KÄ° SAYISAL DEÄžÄ°ÅžKEN ARASINDA GÃ–RSELLEÅžTÄ°RME


#Scatterplot (SaÃ§Ä±lÄ±m grafikleri)

sb.scatterplot(x= "total_bill", y = "tip", data = daf);
#Ã¶denen hesap ve bahÅŸiÅŸ arasÄ±ndaki iliÅŸki 
#Ã–denen hesap ne kadar yÃ¼ksekse bÄ±rakÄ±lan bahÅŸiÅŸte o kadar yÃ¼ksektir


#Ã‡aprazlamalar

sb.scatterplot(x= "total_bill", y = "tip", hue = "time", data = daf);
#AkÅŸam yemeklerinde bÄ±rakÄ±lan bahÅŸiÅŸ daha fazladÄ±r


#style argumanÄ± ile time deÄŸiÅŸkenini simgesel olarak deÄŸiÅŸtiriyor
sb.scatterplot(x= "total_bill", y = "tip", hue = "time", style  ="time", data = daf);

#day Ã¶zelliÄŸinin yanÄ±nda time da eklenir
sb.scatterplot(x= "total_bill", y = "tip", hue = "day", style  ="time", data = daf);

#sadece day Ã¶zelliÄŸi alÄ±nmÄ±ÅŸ
sb.scatterplot(x= "total_bill", y = "tip", hue = "day", style  ="day", data = daf);


sb.scatterplot(x= "total_bill", y = "tip", size = "size", data = daf);

#deÄŸerlere gÃ¶re renklendirme
sb.scatterplot(x= "total_bill", y = "tip", hue = "size", size = "size", data = daf);


#------------------------------------------------------------------------

#DoÄŸrusal Ä°liÅŸkinin GÃ¶sterilmesi

import matplotlib.pyplot as plt

sb.lmplot(x= "total_bill", y = "tip", data = daf);
#iki deÄŸiÅŸken arasÄ±ndaki doÄŸrusal iliÅŸki gÃ¶sterildi

sb.lmplot(x= "total_bill", y = "tip", hue = "smoker", data = daf);

#Ã¶ÄŸÃ¼nlere gÃ¶re daÄŸÄ±lÄ±mÄ±n gÃ¶zlemlenmesi
sb.lmplot(x= "total_bill", y = "tip", hue = "smoker", col = "time", data = daf);


#
sb.lmplot(x= "total_bill", y = "tip", hue = "smoker", col = "time", row = "sex", data = daf);

#------------------------------------------------------------------------

#Scatter Plot Matrisi


#iris Ã§iÃ§ek tÃ¼rlerinin Ã¶zelliklerini ifade eden bir veri seti
iris = sb.load_dataset("iris")
df = iris.copy()
df.head()

df.dtypes
df.shape

#pairplot ile veri setindeki deÄŸiÅŸkenlerin birbirleri arasÄ±ndaki iliÅŸkileri gÃ¶rselleÅŸtirir
sb.pairplot(df);

#oluÅŸturulan grafik toz bulutu ÅŸeklindeyse, yapÄ±sal bir formu yoksa,
#o iki deÄŸiÅŸken arasÄ±nda iliÅŸki olmadÄ±ÄŸÄ± anlamÄ±na gelir

#oluÅŸturulan scatter plot ile oluÅŸturulan gÃ¶zlem noktalarÄ± birbirinde farklÄ± kÃ¶ÅŸelerde kÃ¼meleniyorsa,
#bu kÃ¼meleÅŸmeleri oluÅŸturan farklÄ± alt gruplar vardÄ±r. Bu durumlar gÃ¶z Ã¶nÃ¼ne alÄ±malÄ±

sb.pairplot(df, hue = "species");
#kÃ¼melenmeler bu ÅŸekilde gÃ¶rÃ¼ntÃ¼lenebilir

#markers ile her species Ã¶zelliÄŸi farklÄ± ÅŸekillendirilebilir
sb.pairplot(df, hue = "species", markers = ["o","s","D"]);

#kind ile deÄŸerler arasÄ± ortalamasÄ±nÄ± gÃ¶steren doÄŸru Ã§izilebilir
sb.pairplot(df, hue = "species", kind = "reg");


#------------------------------------------------------------------------

#IsÄ± HaritasÄ± (Heat Map)

#IsÄ± haritasÄ± ile daha geniÅŸ pencereden bakÄ±labilir
#veri seti iÃ§erisinde zaman serisi(gÃ¼n ,ay) verileri olduÄŸunda,
#daha bÃ¼yÃ¼k Ã¶lÃ§ekli velirli periyotlarÄ± takip etmek iÃ§in kullanÄ±lÄ±r

flights = sb.load_dataset("flights")
df = flights.copy()
df.head()

#heatmap fonk yapÄ±sal formda dataframe bekliyor
#bunun iÃ§in pivot tabloya dÃ¶nÃ¼ÅŸtÃ¼rÃ¼lmelidir
#hatalÄ± Ã§Ä±ktÄ±
sb.heatmap(df);

#pivotun ilk iki deÄŸiÅŸkeni x ve y eksenindeki deÄŸerler
#aldÄ±dÄŸÄ± Ã¼Ã§Ã¼ncÃ¼ deÄŸiÅŸken ise kesiÅŸimlerindeki gÃ¶zlemlenmek istenen deÄŸiÅŸkendir
df = df.pivot("month", "year", "passengers");
df
sb.heatmap(df);


#annot ve fmt ile deÄŸerlerin sayÄ±sal ifadeleri gÃ¶sterilebilir
#linewidths ile deÄŸerler arasÄ±na beyaz bir Ã§izgi konulabilir
sb.heatmap(df, annot = True, fmt ="d", linewidths = .5);

#cbar ile sayÄ±larÄ± beliren bar Ã§ubuÄŸu kaldÄ±rÄ±labilir
sb.heatmap(df, annot = True, fmt ="d", linewidths = .5, cbar = False);

#------------------------------------------------------------------------

#LINE PLOT 

#veri seti hikayesi
#beyine baÄŸlanan bir cihaz ile toplanan sinyalleri iade eden veri setidir
#subject verileri toplanan kiÅŸiyi temsil ediyor
#timepoint - zaman noktalarÄ±
#event - verinin toplanmasÄ± ile ilgili farklÄ± olaylarÄ± temsil eder
#region - sinyalin toplandÄ±ÄŸÄ± bÃ¶lge

fmri = sb.load_dataset("fmri")
df = fmri.copy()
df.head()

#herbir zaman noktasÄ±na gÃ¶re signalin durumunu gÃ¶zlemleme
df["timepoint"].describe()
df["signal"].describe()

df.groupby("timepoint")["signal"].count()
#herbir zamanda eÅŸit sayÄ±da sinyal toplanmÄ±ÅŸ
#mekanik bir veri seti olduÄŸu anlaÅŸÄ±labilir

df.groupby("signal").count()
#teil veriler olduÄŸu gÃ¶zlemlenebilir


sb.lineplot(x= "timepoint", y = "signal", data = df);
#koyu mavi Ã§izgi ortalama deÄŸere karÅŸÄ±lÄ±k gelir
#etrafÄ±ndaki aÃ§aÄ±k mavi alan ise standat sapmalarÄ± ile oluÅŸturulmuÅŸ gÃ¼ven aralÄ±klarÄ±nÄ± ifade ediyor


sb.lineplot(x= "timepoint", y = "signal", hue = "event", data = df);
#sÄ±Ã§rama noktalarÄ±nÄ± stim sÄ±nÄ±fÄ± meydana getiriyormuÅŸ


sb.lineplot(x= "timepoint", y = "signal", hue = "event", style = "event", data = df);
#style ile eventleri farklÄ± ÅŸekillerde oluÅŸturulabilir


sb.lineplot(x= "timepoint", y = "signal", hue = "event", style = "event", markers = True, dashes = False, data = df);
#ortalama deÄŸerlerini iÅŸaretleyerek gÃ¶rselleÅŸtirilebilir


sb.lineplot(x= "timepoint", y = "signal", hue = "region", style = "event", data = df);

#------------------------------------------------------------------------

#Basit Zaman Serisi GrafiÄŸi

#indirme iÅŸlemi
!pip install pandas_datareader
import pandas_datareader as pr

#veri setini Ã§ekme - Apple'Ä±n hisse senetleri
df = pr.get_data_yahoo("AAPL", start = "2016-01-01", end = "2019-07-20")
df.head()

kapanis = df["Close"]
kapanis.plot();

kapanis.index
kapanis.index = pd.DatetimeIndex(kapanis.index)
kapanis.head()











