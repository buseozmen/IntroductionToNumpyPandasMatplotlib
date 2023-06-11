import numpy as np
import matplotlib.pyplot as plt

numpyDizisi1 = np.linspace(0,10,20)
print(numpyDizisi1)
numpyDizisi2 = numpyDizisi1 ** 2
print(numpyDizisi2)

(benimFigur, benimEksen) = plt.subplots()
benimEksen.plot(numpyDizisi1,numpyDizisi2, color="#C96F23",alpha= 0.3) #alpha saydamlık küçüldükçe
benimEksen.plot(numpyDizisi2, numpyDizisi1, color="#3A95A8")
plt.show()

(yeniFigur, yeniEksen) = plt.subplots()
yeniEksen.plot(numpyDizisi1,numpyDizisi1 + 2, color="pink", linewidth = 2.0, linestyle = "-.")
yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 3, color="purple", linewidth = 3.0, linestyle = ":")
yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 4, color = "yellow", linestyle = "--" )
yeniEksen.plot(numpyDizisi1,numpyDizisi1 + 5, color="#FF7F00", linewidth = 2.0, linestyle = "-")
yeniEksen.plot(numpyDizisi1,numpyDizisi1 + 7, color="blue", linewidth = 2.0, linestyle = "--",markersize = 8, marker = "o", markerfacecolor ="red" ) #marker + da olabilir
plt.show()

#scatter
plt.scatter(numpyDizisi1,numpyDizisi2)
plt.show()

#histogram
yeniDizi = np.random.randint(0,100,50)
print(yeniDizi)
plt.hist(yeniDizi)
plt.show()

#boxplot
plt.boxplot(yeniDizi)
plt.show()
