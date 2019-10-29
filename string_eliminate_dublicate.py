#to delete the dulicate characters in given string
a=input('enter a string:')
l=len(a)
c=''
for i in range(l):
    if(a[i] not in c):
        c=c+a[i]
    else:
        False
print('output is:',c)
        
    
    
