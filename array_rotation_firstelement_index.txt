#array rotation with first ellement
a=[]
l=int(input('enter length of the lst:'))
for i in range(l):
    a.append(int(input('enter element:')))
b=[]
c=[]
n=a[0]
for i in range(len(a)):
    if(len(a)<n):
            print('limit exceed')
            break
    else:
        if(n<=i):
            c.append(a[i])
        else:
            b.append(a[i])
for i in range(len(b)):
    c.append(b[i])
print('input list is:',a)
print('output list is:',c)
