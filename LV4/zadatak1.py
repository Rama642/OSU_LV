import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import sklearn.linear_model as lm

data = pd.read_csv("data_C02_emission.csv")

#podjelapodataka
features = ['Engine Size (L)', 'Cylinders', 'Fuel Consumption City (L/100km)', 'Fuel Consumption Hwy (L/100km)', 'Fuel Consumption Comb (L/100km)']
target = 'CO2 Emissions (g/km)'

X=data[features]
y=data[target]

#a)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=20)

#b)
def b():

  plt.scatter(X_train['Engine Size (L)'], y_train, color='blue', label='Train')
  plt.scatter(X_test['Engine Size (L)'], y_test, color='red', label='Test')
  plt.xlabel('Engine Size (L)')
  plt.ylabel('CO2 Emissions (g/km)')
  plt.title('CO2 Emissions vs Engine Size')
  plt.legend()
  plt.show()

from sklearn . preprocessing import MinMaxScaler

def c():
#standardizacija skupa za učenje
 

  plt.subplot(2,1,1)
  plt.hist(X_train["Engine Size (L)"], bins=20, color="blue")
  plt.title("Befor scaling - Engine Size")


  scaler= MinMaxScaler()
  X_train_s=scaler.fit_transform(X_train)#1D polje
  X_test_s = scaler.transform(X_test)#1D polje

  X_train_scaled=pd.DataFrame(X_train_s, columns=X_train.columns)
  X_test_scaled= pd.DataFrame(X_test_s, columns= X_test.columns)

  plt.subplot(2,1,2)
  plt.hist(X_train_scaled["Engine Size (L)"], bins=20, color="blue")
  plt.title("After scalign - Engine Size (L)")
  plt.tight_layout()
  plt.show()

#d) Izgradite linearni regresijski modeli. Ispišite u terminal dobivene parametre modela i
  #povežite ih s izrazom 4.6



def d():
  #iz c djela zadatka
  scaler= MinMaxScaler()
  X_train_s= scaler.fit_transform(X_train)
  X_test_s= scaler.fit_transform(X_test)


  linearna_regresija_Model=lm.LinearRegression()
  linearna_regresija_Model.fit(X_train_s, y_train)
  print("Intercept (θ₀):", linearna_regresija_Model.intercept_)
  print("Koeficijenti (θ):", linearna_regresija_Model.coef_)


#e)Izvršite procjenu izlazne veličine na temelju ulaznih veličina skupa za testiranje. 
#Prikažite pomoću dijagrama raspršenja odnos između stvarnih vrijednosti izlazne veličine i procjene dobivene modelom.

def e():

    scaler = MinMaxScaler()
    
    # Ispravno skaliranje
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    # Pretvaranje natrag u DataFrame
    X_train_scaled = pd.DataFrame(X_train_s, columns=X_train.columns)
    X_test_scaled = pd.DataFrame(X_test_s, columns=X_test.columns)

    # Treniranje modela
    model = lm.LinearRegression()
    model.fit(X_train_scaled, y_train)

    # Predikcija na test skupu
    procjena = model.predict(X_test_scaled)

    # Vizualizacija: usporedba stvarnih vs predviđenih vrijednosti
    plt.scatter(y_test, procjena, color="blue")
    plt.title("Real vs Predicted values")
    plt.xlabel("Real label (y_test)")
    plt.ylabel("Predicted label")
    plt.show()




#f)Izvršite vrednovanje modela na način da izračunate vrijednosti regresijskih metrika na skupu podataka za testiranje

def f():
  scaler=MinMaxScaler()
  X_train_s=scaler.fit_transform(X_train)
  X_test_s=scaler.transform(X_test)

  X_train_scaled = pd.DataFrame(X_train_s, columns=X_train.columns)
  X_test_scaled = pd.DataFrame(X_test_s, columns=X_test.columns)

  model= lm.LinearRegression()
  model.fit(X_train_scaled,y_train)

  predikcija= model.predict(X_test_scaled)

  mse = mean_squared_error(y_test, predikcija)
  mae = mean_absolute_error(y_test, predikcija)
  r2 = r2_score(y_test, predikcija)

  print('MSE: ', mse)
  print('MAE: ', mae)
  print("R²: ", r2)



#g)Što se dogada s vrijednostima evaluacijskih metrika na testnom skupu kada mijenjate broj ulaznih veličina?
def g():
  for i, feat in enumerate(features, 1):
    X = data[feat] 
    if isinstance(X, pd.Series): 
        X = X.to_frame()
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = lm.LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Model {i} ({', '.join(feat)}): MSE={mse:.2f}, MAE={mae:.2f}, R²={r2:.4f}")


g()