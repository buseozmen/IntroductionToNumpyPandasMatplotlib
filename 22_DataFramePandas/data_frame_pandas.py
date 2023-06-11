import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(4,3)
print(data)
dataFrame = pd.DataFrame(data)
print(dataFrame)
print(dataFrame[0]) #0. sütunu veriyor
print(type(dataFrame))

yeniDataFrame = pd.DataFrame(data,index=["Buse","Ozgur","Nurdan","Ceyda"], columns= ["Maas","Yas","Calisma Saati"])
print(yeniDataFrame)

print(yeniDataFrame["Yas"])
print(yeniDataFrame["Calisma Saati"])

print(yeniDataFrame[["Maas","Yas"]])

print(yeniDataFrame.loc["Buse"]) #satır çekmek için
print(yeniDataFrame.iloc[2]) #index olarak satırı yazıp bilgisini alıyouz

yeniDataFrame["Emeklilik Yasi"] = yeniDataFrame["Yas"] + yeniDataFrame["Yas"] #sütun ekleme
print(yeniDataFrame)

yeniDataFrame.drop("Emeklilik Yasi", axis = 1)
print(yeniDataFrame) #değişmiyor
yeniDataFrame.drop("Ceyda", axis = 0)
print(yeniDataFrame) #değişmiyor

yeniDataFrame.drop("Emeklilik Yasi", axis = 1, inplace = True) #ana tablodan silmek istiyorsak inplace bool değerini kullanmalıyız
print(yeniDataFrame)

print(yeniDataFrame.loc["Buse"]["Maas"])
print(yeniDataFrame.loc["Nurdan","Yas"]) #her iki şekilde de yazılabilir
print(yeniDataFrame < 0)
booleanFrame = yeniDataFrame < 0
print(booleanFrame)
print(yeniDataFrame[booleanFrame]) #sadece true olan değerleri gösterir
print(yeniDataFrame[yeniDataFrame < 0]) #yukardaki satırla aynı anlamlı kod

print(yeniDataFrame[yeniDataFrame["Yas"] < 0]) #yas kolonunda sadece 0 dan küçük olanları gösterir

print(yeniDataFrame.reset_index()) #yanlarına index bilgisi ekliyor ama kalıcı değil kalıcı olması için inplace

yeniIndexListesi = ["Bus","Ozg","Nur","Cey"]
yeniDataFrame["Yeni Index"] = yeniIndexListesi
print(yeniDataFrame)
print(yeniDataFrame.set_index("Yeni Index")) #kalıcı değil
print(yeniDataFrame)
yeniDataFrame.set_index("Yeni Index", inplace=True) #kalıcı oldu
print(yeniDataFrame)
print(yeniDataFrame.loc["Bus"]) #calisiyor

#multiindex
ilkIndexler = ["Simpson","Simpson","Simpson","South Park","South Park","South Park"]
icIndexler = ["Homer","Bart","Marge","Cartman","Kenny","Kyle"]
birlesmisIndex = list(zip(ilkIndexler,icIndexler))
print(birlesmisIndex)
birlesmisIndex = pd.MultiIndex.from_tuples(birlesmisIndex)
print(birlesmisIndex)
benimCizgiFilmListem = [[40,"A"],[10,"B"],[30,"C"],[9,"D"],[10,"E"],[11,"F"]]
cizgiFilmNumpyDizisi = np.array(benimCizgiFilmListem)
cizgiFilmDataFrame = pd.DataFrame(cizgiFilmNumpyDizisi,index=birlesmisIndex,columns=["Yas","Meslek"])
print(cizgiFilmDataFrame)
print(cizgiFilmDataFrame.loc["South Park"].loc["Kenny"])
cizgiFilmDataFrame.index.names = ["Film Adı","İsim"]
print(cizgiFilmDataFrame)




