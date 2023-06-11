import pandas as pd
import numpy as np

sozlukVerisi = {"Istanbul" : [30,29,np.nan],"Ankara" : [20,np.nan,25],"Izmir" : [40,39,38]}
havaDurumuDataFrame = pd.DataFrame(sozlukVerisi)
print(havaDurumuDataFrame)
havaDurumuDataFrame.dropna() #kalıcı değil orj değişmiyor
print(havaDurumuDataFrame.dropna(axis=1)) #1 demek kolonları alıyor

yeniVeri = {"Istanbul" : [30,29,np.nan],"Ankara" : [20,np.nan,25],"Izmir" : [40,39,38],"Antalya" : [45,np.nan,np.nan]}
yeniDataFrame = pd.DataFrame(yeniVeri)
print(yeniDataFrame)
print(yeniDataFrame.dropna(axis=1,thresh=2)) #kolonlarda 2 nan olanı atıyor, axis row da belirtmene gerek yok
print(yeniDataFrame.fillna(20)) #kalıcı değil inplace yaparsak kalıcı olur
print(yeniDataFrame)

#Groupby
maasSozlugu = {"Departman" : ["Yazilim","Yazilim","Pazarlama","Pazarlama","Hukuk","Hukuk"],"Calisan Ismi" : ["Ahmet","Mehmet","Buse","Burak","Zeynep","Fatma"],"Maas" : [100,150,200,300,400,500]}
maasDataFrame = pd.DataFrame(maasSozlugu)
print(maasDataFrame)
groupObjesi = maasDataFrame.groupby("Departman")
print(groupObjesi.count())
print(groupObjesi.mean("Maas"))
print(groupObjesi.min())
print(groupObjesi.max())
print(groupObjesi.describe())

