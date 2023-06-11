import numpy as np
import pandas as pd

#seriler
benimSozlugum = {"Buse" : 23, "Ozgur" : 47, "Nurdan" : 48}
print(pd.Series(benimSozlugum))
benimYaslarim = [23,47,48]
benimIsimlerim = ["Buse","Ozgur","Nurdan"]
print(pd.Series(benimYaslarim))
print(pd.Series(benimYaslarim, benimIsimlerim))
print(pd.Series(data=benimYaslarim, index=benimIsimlerim)) #karışmaması için böyle yapmak daha sağlıklı

numpyDizisi = np.array([23,47,48])
print(numpyDizisi)
print(pd.Series(numpyDizisi))
print(pd.Series(numpyDizisi,benimIsimlerim))

print(pd.Series(["Ceyda","Busra","Polat"],[1,2,3]))
yarismaSonucu1 = pd.Series([10,5,1],["Ceyda","Busra","Polat"])
print(yarismaSonucu1)
yarismaSonucu2 = pd.Series([20,10,8],["Ceyda","Busra","Polat"])
print(yarismaSonucu2)
print(yarismaSonucu2["Busra"])
sonSonuc = yarismaSonucu1 + yarismaSonucu2
print(sonSonuc)

farkliSeries = pd.Series([20,30,40,50],["a","b","c","d"])
farkliSeries2 = pd.Series([10,5,3,1],["a","c","f","g"])
print(farkliSeries)
print(farkliSeries2)
print(farkliSeries + farkliSeries2) #diğer tarafta bulamadıklarına nan deger atıyor


