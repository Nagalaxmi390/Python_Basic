#left shift with final value is to be added to intial postion of the list by one postion
a=[1,7,3,4,6,5,3]
i=len(a)-1;
while(i>=0):
    t=a[i]
    a[i]=a[i-1]
    a[i-1]=t
    i=i-1
    print(a)
        
