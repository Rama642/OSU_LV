import pandas as pd
import numpy as np

data = pd.read_csv("data_C02_emission.csv")
                     
def a():
  print(data.info()) #piše ti broj podataka koliko ih ima
  print("Broj podataka: ",data.shape[0])

  info = data.info()
  print(info)

  #Postoje li duplicirane ili izostale vrijednosti?
  print(data.isnull().sum())
  print(data.duplicated().sum())
  #ne posotoje duplicirane niti prazne vrijednosti

  #Kategroičke veličine treba grupirati u tip category
  data["Make"]= data["Make"].astype("category")
  data["Model"]= data["Model"].astype("category")
  data["Vehicle Class"]= data["Vehicle Class"].astype("category")
  data["Transmission"]= data["Transmission"].astype("category")
  data["Fuel Type"]=data["Fuel Type"].astype("category")

  print(data.info())


def b():
  consuption=data.sort_values("Fuel Consumption City (L/100km)")
  print("Tri automobila koja imaju najmanju gradsku potrošnju:")
  least=consuption.head(3)
  print(least[["Make","Model","Fuel Consumption City (L/100km)"]])

  print("Tri automobila koja imaju NAJVECU gradsku potrošnju:")
  #maxConsuption=consuption.tail(3)
  print(consuption.tail(3)[["Make","Model","Fuel Consumption City (L/100km)"]])

def c():
  motorSize=data[((data["Engine Size (L)"] >=2.5) &( data["Engine Size (L)"]<=3.5) )]
  counter=motorSize.shape[0]
  print("Ima ",counter,"automobila koji imaju motor u rasponu od [2.5, 3.5] L")
  #prosjecna CO2 emisija
  Emission=motorSize["CO2 Emissions (g/km)"].sum()
  print("Avg CO2 Emission je: ",float(Emission/counter))
  print(motorSize["CO2 Emissions (g/km)"].mean())

def d():
  AudiCars= data[(data["Make"] == "Audi")]
  print("Broj Audi auta je: ", AudiCars.shape[0])
  filtered=AudiCars[AudiCars["Cylinders"]==4]["CO2 Emissions (g/km)"].mean()
  print(filtered)
  filteredAudi= AudiCars[(AudiCars["Cylinders"]== 4)]
  print("Avg Co2 kod Audia je ",filteredAudi["CO2 Emissions (g/km)"].mean())

def e():
  FourSixEight= data[((data["Cylinders"]==4) | (data["Cylinders"] == 6) | (data["Cylinders"]==8))]
  print("Broj vozila s 4,6 i 8 cilindara zajedno: ", FourSixEight.shape[0])

  avgCO2=FourSixEight["CO2 Emissions (g/km)"].mean()
  print(avgCO2)


def f():
  #
  dieaselCars=data[data["Fuel Type"]=="D"]
  GasolineCars=data[(data["Fuel Type"]=="X") | (data["Fuel Type"]=="Z") ]

  print("Avg gradska potrosnja Diesel: ",dieaselCars["Fuel Consumption City (L/100km)"].mean())
  print("Avg gradska potrosnja Benzin: ",GasolineCars["Fuel Consumption City (L/100km)"].mean())

  print("Median gradska potrosnja Diesel: ",dieaselCars["Fuel Consumption City (L/100km)"].median())
  print("Median gradska potrosnja Benzin: ",GasolineCars["Fuel Consumption City (L/100km)"].median())


def g():
  viacle=data[ (data["Cylinders"]== 4) & (data["Fuel Type"]=="D")]
  print(viacle)
  print(max(viacle["Fuel Consumption City (L/100km)"]))
  maxConsuption= viacle.sort_values( by="Fuel Consumption City (L/100km)").tail(1)
  print(maxConsuption)

def h():
  manual=data[(data["Transmission"].str.startswith("M"))].shape[0]
  print("Ima ",manual,"auta s ručnim mjenjačem")

def i():
  print(data.corr(numeric_only=True))

i()