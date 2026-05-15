L=[1,2,3,4,5]
max=L[0]
secondmax=L[0]
for i in L :
  if(i>max):
    secondmax=max
    max=i
  elif(i<max and i>secondmax):
    secondmax=i
  else:
    continue
print(secondmax)