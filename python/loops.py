# last count ni krega 
for i in range(1,10):
    print(i)
    print(i,end="\n")
    print(i,end="\t")
    print(i,end='\v')
    print(i,end="\\")
for k in range(4):
    print(k)
for h in range(10,0,-2):
    print(h)
counter=0
while counter<10:
    print("hi")
    counter+=1
print("???")
# infinte loop
while True:
    print("hi")
    stop=input("stop or not")
    if(stop=="yes"):
        break
    else:
        continue
L=[1,2,3,4,5]
a=1
for i in L:
  a=min(a,i)
print(a)
