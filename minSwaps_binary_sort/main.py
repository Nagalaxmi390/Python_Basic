def miniter(a,n):
    c=0
    while True:
        v=[]
        for i in range(n-1):
            if(a[i]==1 and a[i+1]==0):
                    v.append(i)
        if(len(v)==0):
            break
        else:
            c=c+1
            for i in range(len(v)):
                t=a[v[i]]
                a[v[i]]=a[v[i]+1]
                a[v[i]+1]=t
            #print(a)
    print(c)
t=int(input())
for i in range(t):
    arr=int(input())
    n=int(input())
    a=[int(digit) for digit in str(arr)]
    miniter(a,n)
        