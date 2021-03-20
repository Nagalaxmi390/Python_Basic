#decimal to 8 bit binary conversion
a=int(input('enter a decimal number:'))
b=[]
c=''
d=[]
n=2
e=''
while(a>0):
    b.append(a%n)
    a=a//n
for i in range(8):
    if(len(b)!=8):
        b.append(0)
i=len(b)-1
while(i>=0):
    c=c+str(b[i])
    d.append(b[i])
    i=i-1
print('8 bit binary num is:',c)
#8 bit inary to decimal
dec=0
for i in range(8):
    dec=dec+(d[i]*2**i)
for i in range(8):
    e=e+str(b[i])
print('reverse binary',e)
print('reverse decimal:',dec)
