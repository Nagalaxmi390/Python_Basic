1.#bubble sort in descending order
b=[] #to store the list values
a=int(input('enter a range'))
for i in range(a):
    b.append(int(input('enter a number')))
print(b) #list
for i in range(a):
    for j in range(a):
            if(b[i]>b[j]):
                t=b[i];
                b[i]=b[j];
                b[j]=t;
print(b)



2.#bubble sort in ascending order
b=[] #to store the list values
a=int(input('enter a range'))
for i in range(a):
    b.append(int(input('enter a number')))
print(b) #list
for i in range(a):
    for j in range(a):
            if(b[i]<b[j]):
                t=b[i];
                b[i]=b[j];
                b[j]=t;
print(b)


3.#bubble sort in ascending order
import time
t=(time.time())
b=[] #to store the list values
a=int(input('enter a range'))
for i in range(a):
    b.append(int(input('enter a number')))
print(b) #list
for i in range(a):
    for j in range(a):
            if(b[i]<b[j]):
                t=b[i];
                b[i]=b[j];
                b[j]=t;
print(b)
t1=(time.time())
print(t1-t) #time to taken to comlete sorting 
                
                
                
