
# coding: utf-8

# In[7]:


a=[2,3,4,3,1,2]
a.sort()
print(a)
b=[]
c=[] 
for i in range(len(a)):
    if([i] not in b):
        b.append(a[i])
        c.append(a.count(a[i]))
print(b,c)
        


# In[19]:


s=[(37.21,'Harry'),(37.21,'Berry'),(37.2,'Tina'),(41,'Akriti'),(39,'Harsh')]
s.sort()
print(s)
b=[]
c=[]
a=[]
for i in range(len(s)):
        b.append(s[i][0])
for i in range(len(b)):
    if(b[i] not in a):
        a.append(b[i])
        c.append(b.count(b[i]))
if(c[1]>)

