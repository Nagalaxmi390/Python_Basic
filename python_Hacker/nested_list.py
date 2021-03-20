#LIST LIST OPARATION
n=int(input('length of main list'))
n1=int(input('enter length of first sublist'))
n2=int(input('enter length of second sublist'))
a=[]
b=[]
print('element of first sublist')
for i in range(n1):
    a.append(int(input()))
print(a)
print('elements of second sublist')
for i in range(n2):
    b.append(int(input()))
print(b)
c=list((a,b))
print(c)
