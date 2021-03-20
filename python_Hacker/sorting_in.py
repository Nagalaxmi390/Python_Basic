#sorting
a=int(input('enter a number'))
b=[]
k=0;
for i in range(a):
    b.append(int(input()))
t1=time.time()
print(b)
for i in range(len(b)-1):
        if(b[i]>b[i+1]):
            t=b[i+1]
            b[i+1]=b[i]
            b[i]=t
            for j in range(i):
                    if(b[j]>b[i]):
                        for k in range(i):
                            b[i-k]=b[i-k-1]
                        b[j]=t
print(b)
            
                        
    
        
                
