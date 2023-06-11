import pandas as pd

dataFrame = pd.read_excel("maas.xlsx")
print(dataFrame)

doluDegerlerDataFrame = dataFrame.dropna()
print(doluDegerlerDataFrame)
doluDegerlerDataFrame.to_excel("yenimaas.xlsx")
#read_csv
#to_csv