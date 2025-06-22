def e():
  ind= (data[:,0] == 1) #izdvajanje svih muškaraca
  minH=np.min(data[ind,1])
  maxH=np.max(data[ind,1])
  avgH=np.mean(data[ind,1])
  print("Za muškarce: ")
  print("MinH: ",minHeight,"MaxH: ",maxHeight,"AvgH: ",avgHeight)
