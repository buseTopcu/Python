# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:02:50 2020

@author: Buse TOPÇU
"""

"""

Girdiğim ölçümler içerisinde ortalama ölçüm değeri 170 midir?
H0: mü = 170
H1: mü != 170

T Testi

"""

import numpy as np
import pandas as pd

olcumler = np.array([17, 160, 234, 149, 149, 107, 197, 75, 201, 225, 121, 120, 211, 119, 157, 145, 147, 127, 244, 163, 114, 145,  207,65, 112, 185, 202, 146, 203, 224, 203, 114, 188, 156, 187, 154, 177, 95, 165, 50, 110, 216, 138, 151, 166, 135,  155, 84, 251, 173, 131])

import scipy.stats as st

st.describe(olcumler)

"""Varsayımlar - Normallik Varsayım Testi"""

#Grafik yöntemleriyle Normallik Testi
 
#Histogram
pd.DataFrame(olcumler).plot.hist();


#qqplot
import pylab
st.probplot(olcumler, dist="norm", plot=pylab)

#Noktaların kırmızı çizginin etrafında konumlanması normal dağılımın göstergesidir.

#Test ile Normallik Testi

#Shapiro-Wilks Testi

from scipy.stats import shapiro

shapiro(olcumler)
#çıktı : (0.9848548769950867, 0.7552593946456909)
#ilk değer test istatistiğini, ikinci değer P değerini temsil eder.

#P değeri 0.05 den küçük çıktığında H0 reddedilir.
#Burada H0 reddedilemez. 
"""T Testi UYGULANABİLİR"""

#HİPOTEZ TESTİNİN UYGULANMASI

st.ttest_1samp(olcumler, popmean = 170)

#Çıktı= Ttest_1sampResult(statistic=-2.2287204362493114, pvalue=0.030357490117026445)

#P value değeri kabul edilebilir hata miktarı olarak kabul edilen alfa -0.05- değerinden küçük olduğu için H0 hipotezi reddedilir.
#Ortalama süre 170'den küçüktür

"""Nonparametrik Örneklem Testi"""

#Varsayım sağlanmadığı zaman kullanılır - sign testi

from statsmodels.stats.descriptivestats import sign_test
sign_test(olcumler, 170)

#çıktıdaki ikinci değer 0.05 den küçük olması koşulun sağlanmış olmasını gösterir.


"""
Korelasyon Testi
İki değişken içinde normallik varsayımı
Varsayım sağlanıyorsa Korelasyon Katsayısı
Varsayım sağlanmıyorsa  Spearman Korelasyon Katsayısı

-> Bahşiş İle Ödenen Hesap Arasındaki İlişkinin İncelenmesi

"""

import seaborn as sb
tips = sb.load_dataset("tips")
df = tips.copy()
df.head()

df["total_bill"] = df["total_bill"] - df["tip"]
df.head()

df.plot.scatter("tip", "total_bill");
#toplam hesap arttıkça tip artmış


#KORELASYON KONTROLÜ

from scipy.stats import shapiro

test_istatistigi, pvalue = shapiro(df["tip"])
print("Test İstatistiği = %.4f, p-degeri = %.4f" % (test_istatistigi, pvalue))


test_istatistigi, pvalue = shapiro(df["total_bill"])
print("Test İstatistiği = %.4f, p-degeri = %.4f" % (test_istatistigi, pvalue))

# iki değişken içinde p value değerleri 0.05 den küçük çıktı, normallik varsayımı sağlanmıyor
# H0 Örnek dağılımı ile teorik normal dağılımı olarak istatistiki olarak anlamlı bir farklılık yoktur.
# Ho reddedildi. Anlamlı bir farklılık vardır bu nedenle dağılımlar birbirine benzemiyor
# Normallik varsayımı sağlanmamaktadır


#Korelasyon Katsayısı

df["tip"].corr(df["total_bill"])
#corr fonk ön tanımlı olarak Pearson Kolerasyon Katsayısını verir
#Pearson normallik katsayısı sadece değişkenler için normallik varsayımı sağlandığında hesaplanabilir

df["tip"].corr(df["total_bill"], method = "spearman")
#spearman Korelasyon Katsayısı

"""
#Korelasyon Anlamlılık Testi

from scipy.stats import pearsonr

test_istatistigi, pvalue = shapiro(df["tip"])
print("Kolerasyon Katsayısı = %.4f, p-degeri = %.4f" % (test_istatistigi, pvalue))

 
test_istatistigi, pvalue = shapiro(df["total_bill"])
print("Test İstatistiği = %.4f, p-degeri = %.4f" % (test_istatistigi, pvalue))

#Pearson Kolerasyon Katsayısına göre gerçekleştirildi
# Değişkenler arasında anlamlı bir farklılık yoktur diyen H0 reddedildi(pearson Kolerasyon katsayısına göre)

"""

#Nonparametrik kolerasyon hipotez testi

st.spearmanr(df["tip"], df["total_bill"])
#P value değeri küçüktür. Değişkenler arasında ilişki yoktur diyen H0 hipotezi reddedilir

kor_kat, pvalue = st.spearmanr(df["tip"], df["total_bill"])
print("Kolerasyon Katsayısı = %.4f, p-degeri = %.4f" % (kor_kat, pvalue))

#Değişkenler arasında anlamlı bir farklılık yoktur diyen H0 reddedildi
#Pozitif yönde anlamlı bir ilişki vardır


#kendalltau testi de yapılabilir
kor_kat, pvalue = st.kendalltau(df["tip"], df["total_bill"])
print("Kolerasyon Katsayısı = %.4f, p-degeri = %.4f" % (kor_kat, pvalue))











