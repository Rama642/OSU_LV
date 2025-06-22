import numpy as np
import matplotlib.pyplot as plt

def pr1():
  a= np.array( [2,3,4])
  print(type(a))
  print(a.shape)
  print(a[0], a[1], a[2])
  a[0]=5
  print(a)
  print(a[1:2])
  print(a[1:-1])
  print("")
  b= np.array([[1,2,3], [5,1,2]])
  print(b)
  print("")
  print(b.shape)
  print("")

  print( b[0,2], b[0,1], b[1,1])  
  print( b[0:2, 0:1] )
  print( b[:,0:2])


def pr2():
  c=np.ones((4,2), np.float32)
  print(c)
  d=np.zeros((4,2))
  print(d)
  e=np.eye(5)
  print(e)

  g=np.array([1,2,3], np.float32)
  print(len(g))
  h=g.tolist()
  print(h)
  print(c.transpose())
  E=np.array([5,9,3])

  z=np.concatenate((g,E))
  print(z)


def pr3():
  a=np.array([1,2,3], np.float32)
  b=np.array([3,9,4], np.float32)

  print(a+b)
  print("")
  print(a-b)
  print("")

  print(a*b)
  print("")
  print(a/b)
  print("")
  print("")
  print(np.mean(a))


def pr4():
 
  
  x = np.linspace(0, 6, num=30)
  y = np.sin(x)

  plt.plot(x, y, 'b', linewidth=1, marker=".", markersize =5)

  plt.axis([0,6,-2,2])
  plt.xlabel('x')
  plt.ylabel('vrijednosti funkcije')
  plt.title('sinus funkcija ')
  plt.show()


def pr5():
  
  img = plt.imread("road.jpg")
  Slika2D = img[:,:,0].copy()
  print(img.shape)
  print(img.dtype)

  plt.figure()
  plt.imshow(Slika2D , cmap="gray")
  plt.show()


