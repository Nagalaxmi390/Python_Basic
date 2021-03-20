#to sort the elements given by the user in a nested list with out using inbuilt functions
n=int(input('enter a length of main lists'))
b=[]
a=[]
out=[]
temp=0
for i in range(n):
    a.append(b) #forming a empty sublist
print(a)
print('enter length of the sub lists')
l=[] #for length storing
for i in range(n):
        l.append(int(input()))
print(l)
#passing vaues to the empty lists
for i in range(n):
    c=[]
    print('enter list elemnts of the lost',i)
    for j in range(l[i]):
        c.append(int(input()))
    a.append(c)
del(a[0:n])
print(a)
#sorting the elements in nested list
for i in range(n):
    for j in range(l[i]-1):
        for k in range(l[i]-1):
            if(a[i][k]>a[i][k+1]):
                temp=a[i][k+1]
                a[i][k+1]=a[i][k]
                a[i][k]=temp
print(a)

