import numpy as np
import pandas as pd

sozluk1 = {"Isim" : ["Ahmet","Mehmet","Zeynep","Atıl"],"Spor" : ["Koşu","Yüzme","Koşu","Basketbol"],"Kalori" : [100,200,300,400]}
dataFrame1 = pd.DataFrame(sozluk1,index= [0,1,2,3])

sozluk2 = {"Isim" : ["Osman","Levent","Atlas","Fatma"],"Spor" : ["Koşu","Yüzme","Koşu","Basketbol"],"Kalori" : [200,100,50,300]}
dataFrame2 = pd.DataFrame(sozluk2, index= [4,5,6,7])

sozluk3 = {"Isim" : ["Ayşe","Mahmut","Duygu","Nur"],"Spor" : ["Koşu","Yüzme","Badminton","Tenis"],"Kalori" : [300,400,500,250]}
dataFrame3 = pd.DataFrame(sozluk3, index= [8,9,10,11])

#concatenation
print(pd.concat([dataFrame1,dataFrame2,dataFrame3],axis=0)) #satır birleşmesi axis = 0

#merge (kaynaştırmak)
mergeSozluk1 = {"Isim" : ["Ahmet","Mehmet","Zeynep","Atil"],"Spor" : ["Koşu","Yüzme","Koşu","Basketbol"]}
mergeDataFrame1 = pd.DataFrame(mergeSozluk1)
print(mergeDataFrame1)

mergeSozluk2 = {"Isim" : ["Ahmet","Mehmet","Zeynep","Atil"],"Kalori" : [100,200,150,250]}
mergeDataFrame2 = pd.DataFrame(mergeSozluk2)
print(mergeDataFrame2)

print(pd.merge(mergeDataFrame1,mergeDataFrame2,on = "Isim"))


maasSozluk = {"Isim" : ["Atil","Zeynep","Mehmet","Ahmet"],"Departman" : ["Yazilim","Satis","Pazarlama","Yazilim"],"Maas" : [200,300,400,500]}
maasDataFrame = pd.DataFrame(maasSozluk)
print(maasDataFrame)

print(maasDataFrame["Departman"].unique())
print(maasDataFrame["Departman"].nunique()) #kaç farklı
print(maasDataFrame["Departman"].value_counts()) #hangi departmanda kaç tane

def bruttenNete(maas):
    return maas*0.66

print(maasDataFrame["Maas"].apply(bruttenNete)) #uygula komutu
print(maasDataFrame.isnull()) #null deger var mı

yeniBirVeri = {"Karakter Sınıfı" : ["South Park","South Park","Simpson","Simpson","Simpson"],"Karakter Ismi" : ["Cartman","Kenny","Homer","Bart","Bart"],"Karakter Yas" : [9,10,50,20,10]}
karakterDF = pd.DataFrame(yeniBirVeri)
print(karakterDF)
print(karakterDF.pivot_table(values="Karakter Yas", index= ["Karakter Sınıfı","Karakter Ismi"],aggfunc=np.sum)) #ortalama almasın diye toplamayı belirttik


