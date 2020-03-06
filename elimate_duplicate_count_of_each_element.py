
# coding: utf-8

# In[7]:



a=[2,3,4,3,1,2]
a.sort()
print(a)
b=[]
c=[] 
for i in range(len(a)):
    if(a[i] not in b):
        b.append(a[i])
        c.append(a.count(a[i]))
print(b,c)
        

