#after every turns letter get change of alfabet anf if it was odd number it has to chage
a=[1,2,4,1,3,1,1,4,6,0,0,1,1,1,2,1,0,6,0,0,1,2,1,0,0,4,0,1,0]
 #here d,s changers
c=['d']
for i in range(0,len(a)-1):
    if(i==5| i==11| i==17 | i==23):
            if(c[-1]=='s'):
                c.append('d')
            else:
                c.append('s')
    elif(a[i]%2==1):
            if(c[-1]=='d'):
                c.append('s')
            else:
                c.append('d')
    else:
        c.append(c[-1])
print(len(a),len(c))
print(c)
print(a)
d=0
s=0
for i in range(len(a)-1):
    if(c[i]=='d'):
        d=d+a[i]
    else:
        s=s+a[i]
print('score of d',d)
print('score of s',s)
        
