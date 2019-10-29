#to find factorial of the given number
a=int(input('enter a number:'))
f=1
for i in range(a):
    f+=f*i;
print('factorial:',f)

#to finf factorial of the given number up to the range
a=int(input('enter a number:'))
f=1
fact=[]
for i in range(a):
    f+=f*i;
    fact.append(f)
print('factorial:',fact)
