import numpy as np
benimDizim = np.arange(0,15)
print(benimDizim)
print(benimDizim[5])

print(benimDizim[3:8])
benimDizim[3:8] = -5
print(benimDizim) # direkt dizinin içerisinde değişiyor

baskaDizi = np.arange(0,24)
print(baskaDizi)
slicingDizisi = baskaDizi[4:9]
print(slicingDizisi)

slicingDizisi[:] = 700 #elemanları değiştiriyor
print(slicingDizisi)
print(baskaDizi) #burada da elemanlar değişiyor orj değişiyor

ornekDizi = np.arange(0,24)
print(ornekDizi)
ornekDiziKopyasi = ornekDizi.copy() #orj değişmesin diyosan copyle çalış
print(ornekDiziKopyasi)
ornekDiziKopyasiSlicing = ornekDiziKopyasi[3:6]
print(ornekDiziKopyasiSlicing)
ornekDiziKopyasiSlicing[:] = 800
print(ornekDiziKopyasiSlicing)
print(ornekDiziKopyasi) #kopyası değişti
print(ornekDizi) #orj dizi değişmedi

#matrix
benimListem = [[10,20,30],[20,30,40],[40,50,60]]
benimMatrixDizim = np.array(benimListem)
print(benimMatrixDizim)
print(benimMatrixDizim[0])
print(benimMatrixDizim[1][2])
print(benimMatrixDizim[1,2]) #bu şekilde de yazılabilir

print(benimMatrixDizim[1:,2]) #1. satırdan sonuncu satıra kadar 2. indexleri getir
print(benimMatrixDizim[0:,2]) #0. satırdan sonuncuya kadar 2. indexleri getir
print(benimMatrixDizim[2:,2])
print(benimMatrixDizim[2:,1:]) #2. satırdan sonuncuya kadar 1. indexten sonuncu indexe kadar alır

yeniListe = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
yeniMatrix = np.array(yeniListe)
print(yeniMatrix)
print(yeniMatrix[2]) #2.satır
print(yeniMatrix[[4,2,0]]) #4 2 ve 0. satırları verir

#operasyonlar
yeniBirDizi = np.random.randint(1,100,20)
print(yeniBirDizi)
sonucDizisi = yeniBirDizi > 24
print(sonucDizisi) #bool değer döndürüyor sonuç değiştirmiyor
print(yeniBirDizi[sonucDizisi]) #falseları vermiyor
yeniBirDizi[yeniBirDizi>24] #yukarı satırla aynı

sonDizi = np.arange(0,24)
print(sonDizi)
print(sonDizi + sonDizi)
print(sonDizi * sonDizi)
print(sonDizi - sonDizi)
print(sonDizi / sonDizi)  # 0/0 tanımsız olduğu için hata verebilir yoksa nan yazar
print(np.sqrt(sonDizi))
print(np.max(sonDizi))
print(np.min(sonDizi))