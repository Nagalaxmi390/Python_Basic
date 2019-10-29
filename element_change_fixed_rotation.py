#after every turns letter get changed
a=[1,2,4,1,3,1,1,4,6,0,0,1,1,1,2,1,0,6,0,0,1,2,1,0,0,4,0,1,0]
c=['d'] #here d,s changers
for i in range(1,len(a)-1):
    if(i%6==0):
            if(c[-1]=='d'):
                 c.append('s')
            else:
                c.append('d')
print(c)
print(a)
print(len(a))
