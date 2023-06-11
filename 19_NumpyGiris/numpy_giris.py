import numpy as np

#numpy array
benimListem = [20,30,40]
print(type(benimListem))

print(np.array(benimListem))

matrixListesi = [[10,20,30],[20,30,40],[30,40,50]]
print(matrixListesi[1][0])

print(np.array(matrixListesi))

#arange*
print(list(range(0,10)))

print(np.arange(0,10))
print(np.arange(0,20,2))

#zeros
print(np.zeros(5))
print(np.zeros((2,2)))
print(np.zeros((9,9)))

print(np.ones(5))
print(np.ones((9,9)))

#linspace*
print(np.linspace(0,20,5)) #5 elemanla yaz demek
print(np.linspace(0,10,30)) #10 u dahil ediyor

#eye
print(np.eye(3))

#random
print(np.random.randn(4))
print(np.random.randn(4,4))

print(np.random.randint(1,10)) #10 u almaz
print(np.random.randint(1,300,5)) #5 elemanla göster demek

benimNumpyDizim = np.arange(30)
print(benimNumpyDizim)

benimRandomDizim = np.random.randint(0,100,20)
print(benimRandomDizim)

#numpy dizi methodları
print(benimNumpyDizim.reshape(5,6))

print(benimNumpyDizim.max())
print(benimRandomDizim.max())
print(benimRandomDizim.min())
print(benimRandomDizim.argmax()) #dizideki sırasını veriyor
print(benimRandomDizim.argmin()) #dizideki sırasını veriyor

 