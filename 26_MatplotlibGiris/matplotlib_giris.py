import numpy as np
import matplotlib.pyplot as plt

yasListesi = [10,20,30,30,30,40,50,60,70,75]
kiloListesi = [20,60,80,85,86,87,70,90,95,90]
numpyYasListesi = np.array(yasListesi)
numpyKiloListesi = np.array(kiloListesi)
grafik1 = plt.plot(numpyYasListesi,numpyKiloListesi,"b") #b blue, g green, r red, y yellow, ilk yazdığın x ekseni diğeri y ekseni
plt.xlabel("Yas")
plt.ylabel("Kilo")
plt.title("Kilonun Yaşa Göre Değişim Grafiği")
plt.show() #bakmak için aktif hale getir


numpyDizisi1 = np.linspace(0,10,20)
print(numpyDizisi1)
numpyDizisi2 = numpyDizisi1 ** 3
print(numpyDizisi2)
grafik2 = plt.plot(numpyDizisi1,numpyDizisi2,"g*-") #--,-*
plt.show()
plt.subplot(1,2,1)
plt.plot(numpyDizisi1,numpyDizisi2,"r*-")
plt.subplot(1,2,2) #1 sıra olacak, 2 kolon olacak, şuan 2. grafiği çiziyorum
plt.plot(numpyDizisi2,numpyDizisi1,"g--")
plt.show()

benimFigure = plt.figure()
figureAxes = benimFigure.add_axes([0.8,0.8,0.3,0.3])
figureAxes.plot(numpyDizisi1,numpyDizisi2,"g")
figureAxes.set_xlabel("X Ekseni Veri İsmi")
figureAxes.set_ylabel("Y Ekseni Veri İsmi")
figureAxes.set_title("Grafik Başlığı")
plt.show()

figure2 = plt.figure()
eksen1 = figure2.add_axes([0.1,0.1,0.9,0.9]) #burayla oynayarak boyut ayarlanabilir
eksen2 = figure2.add_axes([0.2,0.5,0.3,0.3])

eksen1.plot(numpyDizisi1,numpyDizisi2,"g")
eksen1.set_xlabel("X Ekseni")
eksen1.set_ylabel("Y Ekseni")
eksen1.set_title("Ana Grafik Başlık")

eksen2.plot(numpyDizisi2,numpyDizisi1,"b")
eksen2.set_xlabel("X Ekseni")
eksen2.set_ylabel("Y Ekseni")
eksen2.set_title("Küçük Grafik Başlık")
plt.show()

(benimFigurem, benimEksenler) = plt.subplots(nrows=1,ncols=2) #boş eksen çıkıyor
#benimEksenler.plot(numpyDizisi1,numpyDizisi2,"b")
for eksen in benimEksenler:
    eksen.plot(numpyDizisi1,numpyDizisi2,"g")
    eksen.set_xlabel("X Ekseni")
plt.tight_layout() #daha düzgün gvösteriyor aralarındaki aralığı ayarlıyor
plt.show()

yeniFigur = plt.figure() #figsize parametresi verilebilir figsize = (3,3), dpi = 100 çözünürlük değeri büyük oldukça kaliteli
yeniEksen = yeniFigur.add_axes([0.1,0.1,0.9,0.9])
yeniEksen.plot(numpyDizisi1,numpyDizisi1 ** 2, label = "numpyDizisi ** 2") #başka çizgiler olursa karışıklık önlemek için label atanır
yeniEksen.plot(numpyDizisi1,numpyDizisi1 ** 3, label = "numpyDizisi ** 3")
yeniEksen.legend(loc=1) #lokasyon verebilirsin
plt.show()
yeniFigur.savefig("benimfigur.png", dpi=200) #kaydetme




