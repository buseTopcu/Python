# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:18:33 2020

@author: Buse TOPÇU
"""
import pandas as pd
import seaborn as sb


dataFrame = pd.read_csv("Mall_Customers.csv")
mallCustomer = dataFrame.copy()
mallCustomer.columns
mallCustomer.head()
mallCustomer.describe()

""" Yıllık gelir miktarı 61 k$ mıdır? 

H0: mü = 61
H1: mü != 61

T Testi
"""

mallCustomer.isnull().sum()
# null deger bulunmamaktadır


""" Normallik Varsayım Testi """

import pylab
import scipy.stats as st
st.probplot(mallCustomer["Annual Income (k$)"], dist="norm", plot=pylab);
### Age degerlerinin Annual Income (k$) egrisinin etrafında konumlanması normal dağılımın göstergesidir


""" Shapiro-Wilks Testi ile Normallik Varsayımı Uygulanması
 
H0: ornek dagılımı ile teorik dagılımı arasında istatistiksel olarak bir fark yoktur 
H1: Fark vardır.
"""

from scipy.stats import shapiro

#shapiro(df["Annual Income (k$)"])
print("T istatistiği: " + str(shapiro(mallCustomer["Annual Income (k$)"])[0]))
print("P value: " + str(shapiro(mallCustomer["Annual Income (k$)"])[1]))
### ilk değer test istatistiğini, ikinci değer P değerini temsil eder
# P değeri 0.05 den küçük çıktığından dolayı H0 reddedilir.
""" ornek dagılımı ile teorik dagılımı arasında istatistiksel olarak bir fark VARDIR """


sb.distplot(mallCustomer["Annual Income (k$)"], kde = False);
sb.distplot(mallCustomer["Annual Income (k$)"]);

""" 
T testi uygulanamaz 
T-testi ile varsayımın sağlanmadığı durumda Nonparametrik tek örneklem test kullanılır.
Bu testlerden biri olan Sign Testini uygulayacağım.
"""


""" SIGN TESTİ """

from statsmodels.stats.descriptivestats import sign_test

test_istatistigi, pvalue = sign_test(mallCustomer["Annual Income (k$)"], 61)
print("Test İstatistiği = %.7f, p-degeri = %.7f" % (test_istatistigi, pvalue))
# P deger 0.05 den buyuk H0 hipotezi kabul edilir.


#------------------------------------------------------------------------------------------------------


dataFrame = pd.read_csv("online_shoppers_intention.csv")
shop = dataFrame.copy()
shop.columns


""" Siteden çıkma oranı ortalama 0.04 sn midir? 

H0: mü = 0.04
H1: mü != 0.04

T-Testi
"""


shop["ExitRates"].mean()


shop.columns
shop.head()
shop.describe()

shop.isnull().sum()
# BounceRates degeri Bir web sayfasının Hemen Çıkma Oranlarını temsil ediyor
# bu deger icerisinde 14  adet null deger var 


shop["ExitRates"].fillna(shop["ExitRates"].mean(), inplace=True)
shop.isnull().sum()
# null degerlerini ExitRates'in ortalama degerleri ile doldurdum

shop.dropna(subset=['ExitRates'], how='all', inplace=True)


sb.barplot(x = "ExitRates", y = "Month", data = shop);


""" SHAPIRO TESTI """

print("P value: " + str(shapiro(shop["ExitRates"])[1]))
# P değeri 0.05 den buyuk çıktığından dolayı H0 KABUL EDILIR.
""" T-testi uygulanabilir """


""" T-TESTI UYGULAMASI """

test_istatistigi, pvalue = st.ttest_1samp(shop["ExitRates"], popmean = 0.04)
print("Test İstatistiği = %.7f, p-degeri = %.7f" % (test_istatistigi, pvalue))
# P değeri 0.05 den küçük çıktığında H0 reddedilir. 

# P value değeri kabul edilebilir hata miktarı olarak kabul edilen alfa -0.05- değerinden kucuk,
# bu nedenle H0 hipotezi reddedilir.

"""
H0 hipotezini reddettik. 
Siteden çıkma oranı ortalama 0.04 sn den farklı olduğunu istatistiksel olarak ortaya koyduk.

"""

#------------------------------------------------------------------------------------------


"""
Korelasyon Testi
İki değişken içinde normallik varsayımı gerçekleştirilir
Varsayım sağlanıyorsa Pearson Korelasyon Katsayısı kullanılır
Varsayım sağlanmıyorsa  Spearman Korelasyon Katsayısı kullanılır

-> Yaş ile Kazanç Arasındaki İlişkinin İncelenmesi



H0: Yaş ile kazanç arasında anlamlı bir ilişki -korelasyon- yoktur (ro = 0)
H1: Yaş ile kazanç arasında anlamlı bir ilişki vardır  (ro != 0) - dağılımlar birbirine benzemez

"""

dataFrame = pd.read_csv("Mall_Customers.csv")
mallCustomer = dataFrame.copy()


sb.lmplot(x= "Annual Income (k$)", y = "Age", hue = "Genre", data = mallCustomer);

from scipy.stats import shapiro

test_istatistigi, pvalue = shapiro(mallCustomer["Annual Income (k$)"])
print("Test İstatistiği = %.4f, p-degeri = %.4f" % (test_istatistigi, pvalue))

test_istatistigi, pvalue = shapiro(mallCustomer["Age"])
print("Test İstatistiği = %.4f, p-degeri = %.4f" % (test_istatistigi, pvalue))
# p degerleri 0.05 den küçük çıktı, normallik varsayımı sağlanmıyor


""" Korelasyon Katsayısı Hesaplama """


mallCustomer["Annual Income (k$)"].corr(mallCustomer["Age"])
# Pearson Korelasyon Katsayısı

mallCustomer["Annual Income (k$)"].corr(mallCustomer["Age"], method = "spearman")
#corr fonk ön tanımlı olarak Pearson Kolerasyon Katsayısını verir
#Pearson normallik katsayısı sadece değişkenler için normallik varsayımı sağlandığında hesaplanabilir
# Bu nedenle spearman korelasyon katsayısını belirtmeliyiz



""" Kolerasyon Hipotez Testleri """


from scipy.stats import pearsonr

test_istatistigi, pvalue = pearsonr(mallCustomer["Annual Income (k$)"], mallCustomer["Age"])
print("Kolerasyon Katsayısı = %.4f, p-degeri = %.4f" % (test_istatistigi, pvalue))

#Pearson Kolerasyon Katsayısına göre gerçekleştirildi
# Değişkenler arasında anlamlı bir farklılık yoktur diyen H0 reddedildi


import scipy.stats as st


kor_kat, pvalue = st.spearmanr(mallCustomer["Annual Income (k$)"], mallCustomer["Age"])
print("Kolerasyon Katsayısı = %.4f, p-degeri = %.4f" % (kor_kat, pvalue))

# p degeri alfa degeri olan 0.05 den buyuk oldugu için H0 kabul edilir
# Degiskenler arasında istatiksel bir anlamlılık yoktur.


#kendalltau testi de yapılabilir
kor_kat, pvalue = st.kendalltau(mallCustomer["Annual Income (k$)"], mallCustomer["Age"])
print("Kolerasyon Katsayısı = %.4f, p-degeri = %.4f" % (kor_kat, pvalue))



