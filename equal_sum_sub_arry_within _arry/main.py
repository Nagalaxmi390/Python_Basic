def Sum(x):
    c=1
    b=[]
    n=len(x)
    for i in range(n//2):
        b.append(([x[i],x[n-1-i]]))
    for i in range(len(b)-1):
        if(sum(b[i])==sum(b[i+1])):
            c=c+1
    if((n//2)==c):
        print(c)
    else:
        print("No")
x = list(map(int,input().split()))
x.sort(reverse=True)#ascending order of the elements
if(len(x)%2==0):
    Sum(x)
else:
    x.append(0)
    Sum(x)
    
            
    