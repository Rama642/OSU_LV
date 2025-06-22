import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("data_C02_emission.csv")

def a():
  plt.figure()
  data["CO2 Emissions (g/km)"].plot(kind="hist",bins=20)
  plt.show()

def b():
  data['Fuel Type'] = data['Fuel Type'].astype('category')
  data.plot.scatter(x = 'Fuel Consumption City (L/100km)',
                  y = 'CO2 Emissions (g/km)',
                  c = 'Fuel Type', cmap = 'cool', s = 20)
  plt.title("Diagram Fuel Consumption - CO2 Emission")
  plt.show()
  
def c():
  data.boxplot(column=["Fuel Consumption Hwy (L/100km)"], by="Fuel Type")
  plt.show()


def d():
  fuel_counts = data.groupby('Fuel Type').size()
  fuel_counts.plot(kind='bar', color="lightblue", edgecolor="purple")
  plt.title("Diagram Vehicles - Fuel Type")
  plt.show()


def e():
  avg_co2 = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
  avg_co2.plot(kind = 'bar', color='red',edgecolor='purple')
  plt.title("Diagram CO2 Emission - Cylinders")
  plt.show()


e()