2.#arranging the elements in the list in dictionary arder
b=['amma','nanna','akka']
for i in range(len(b)):
    for j in range(len(b)):
            if(b[i]<b[j]):
                t=b[i]
                b[i]=b[j]
                b[j]=t
print(b)#['amma','akka','nanna']
