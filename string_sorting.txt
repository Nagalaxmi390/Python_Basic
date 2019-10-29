#string_sorting
a=input('enter a string:')
b=[]
out=''
for i in range(len(a)):
    b.append(a[i])
for i in range(len(a)):
    for j in range(len(a)):
        if(b[i]<b[j]):
            t=b[j]
            b[j]=b[i]
            b[i]=t
for i in range(len(b)):
    out=out+b[i]
print('inut:',a,'\n','output:',out)
#expected out is
	#enter a string:ammananna
	#inut: ammananna 
 	#output: aaaammnnn

            
