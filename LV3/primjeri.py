import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pr1():
  s1 = pd.Series(['crvenkapica ', 'baka', 'majka', 'lovac ', 'vuk'])
  print(s1)

  s2 = pd.Series(5., index =['a','b','c','d','e'], name = 'ime_objekta ')
  print(s2)
  print(s2['b'])

  s3 = pd.Series(np.random.randn(5))
  print(s3)
  print(s3[3])

def pr2():
  rjecnik= { 'country':["Italy", "Spain", "Greece", "France", "Portugal"],
          "population": [59,47,11,68,10],
          "code": [39,34,30,33,351]
         }
  countries=pd.DataFrame(rjecnik, columns=["country","population","code"])
  print(countries)

  print(countries.info())
  print(countries.head(2))
  print(countries.tail(2))

  print("")
  print("") 
  print("")

  print(countries.describe())
  print(countries.min())
  print(countries.max())

def pr3():
  data=pd.read_csv("data_C02_emission.csv")
  print(data.Cylinders)
  print("")
  print("")
  print(data[["Model", "Cylinders"]])

  print(data.iloc[2:6, 2:7])
  print(data.iloc[:,2:5])
  print(data.iloc[:, [0,4,7]])
  print("")
  print("")

  print(data[data.Cylinders > 6])


def pr4():
  data=pd.read_csv("data_C02_emission.csv")
  new_data=data.groupby("Cylinders")

  print(new_data.count())
  print(new_data.size())
  print(new_data.sum())


def pr5():
  data=pd.read_csv("data_C02_emission.csv")
  print(data.isnull().sum())
  data.dropna(axis=0)
  print(data.isnull().sum())
  data.dropna(axis=1)

  

def pr6():
  data=pd.read_csv("data_C02_emission.csv")
  plt.figure()
  data['Fuel Consumption City (L/100km)'].plot(kind='hist', bins = 20)
  plt.figure()
  data['Fuel Consumption City (L/100km)'].plot(kind="box")
  plt.show()

def pr7():
  data = pd.read_csv('data_C02_emission.csv')
  grouped = data.groupby('Cylinders')
  grouped.boxplot(column =['CO2 Emissions (g/km)'])
  data.boxplot(column =['CO2 Emissions (g/km)'], by='Cylinders')
  plt.show()



def pr8():
  data = pd.read_csv('data_C02_emission.csv')
  data.plot.scatter(x="Fuel Consumption City (L/100km)",
                    y="Fuel Consumption Hwy (L/100km)",
                    c="Engine Size (L)", cmap="hot", s=50
                    )
  plt.show()
  print(data.corr(numeric_only=True))


  
