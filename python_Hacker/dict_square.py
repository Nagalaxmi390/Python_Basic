#store the squares of the values in dictionary
a=int(input('enter the range'))
b={}
for i in range(a):
    b[i]=i*i
print(b)

#store the squares of the values in tuples using lists
a=int(input('enter the range'))
b=[]
for i in range(a):
    b.append(i)
    c=tuple(b)
print(c)
