#decimal to 8 bit binary conversion
a=int(input('enter a decimal number'))
b=[]
c=''
n=2
while(a>0):
    b.append(a%n)
    a=a//n
for i in range(8):
    if(len(b)!=8):
        b.append(0)
i=len(b)-1
while(i>=0):
    c=c+str(b[i])
    i=i-1
print('8 bit binary num is:',c)
    
