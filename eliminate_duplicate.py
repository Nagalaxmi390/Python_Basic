a=[1,2,3,1,2]
c=0
d=[]
for i in range(len(a)):
    if(a[i] not in d):
            d.append(a[i])
print(d)
    
