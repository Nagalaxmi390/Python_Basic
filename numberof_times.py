﻿#task:find the s integer repeats in given n range

#example in the range 100 how may times 3 can be written. ans 20

b=[]

c=0

n=int(input('ener range'))

s=input('enter a character to check')

for i in range(n):
       
	 b.append(str(i))

for i in range(100):
   
	 for j in range(len(b[i])):
        
		if(s in b[i][j]):
                
			c=c+1

print(c)
