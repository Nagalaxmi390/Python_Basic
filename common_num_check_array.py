#to check the wether common number is present in the both the arrays are not
a=[1,2,3,1]

b=[3,2,1,4]

c=[]

for i in range(max(len(a),len(b))):

    if(b[i] in a):
            
	print(True)
   
     else:
            
	print(False)
