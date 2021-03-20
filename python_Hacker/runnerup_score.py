
# coding: utf-8

# In[9]:


a=[1,222,1,2,12]
b=[]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if(a[j]<a[j+1]):
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print(a[-2])


# In[11]:


a=[1,222,333,11,333]
a.sort()
print(a)
b=[]
for i in range(len(a)):
    if(a[i] not in b):
        b.append(a[i])
print('runner score',b[-2])

