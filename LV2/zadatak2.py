import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.csv", delimiter=",", skiprows=1)

numOfPeople= data.shape[0]
print("Number of people: ",numOfPeople)

def b():
  plt.scatter(data[:,1],data[:,2], alpha=0.5, color="red")
  plt.title("Odnos visine i mase")
  plt.xlabel("Visina")
  plt.ylabel("Težina")
  plt.show()

def c():#potrebno je prikazati za svaku 50. osobu
  plt.scatter(data[::50,1], data[::50,2], alpha=1, color="yellow")
  plt.title("Odnos visine i mase za svaku 50. osobu")
  plt.xlabel("Visina")
  plt.ylabel("Težina")
  plt.show()

  #data[start: stop: Step]

def d():
  minHeight=np.min(data[:,1])
  maxHeight=np.max(data[:,1])
  avgHeight=np.mean(data[:,1])
  print("MinH: ",minHeight,"MaxH: ",maxHeight,"AvgH: ",avgHeight)

def e():
  ind= (data[:,0] == 1) #izdvajanje svih muškaraca
  minH=np.min(data[ind,1])
  maxH=np.max(data[ind,1])
  avgH=np.mean(data[ind,1])
  print("Za muškarce: ")
  print("MinH: ",minH,"MaxH: ",maxH,"AvgH: ",avgH)

  print("Za žene: ")
  ind_ž= (data[:,0]== 0)
  minH=np.min(data[ind_ž,1])
  maxH=np.max(data[ind_ž,1])
  avgH=np.mean(data[ind_ž,1])
  
  print("MinH: ",minH,"MaxH: ",maxH,"AvgH: ",avgH)


e()