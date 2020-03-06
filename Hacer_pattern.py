
# coding: utf-8

# In[19]:


import cmath
cmath.phase(complex(-1.0, 0.0))


# In[91]:


print(u'\u00b0')


# In[82]:


import math
from cmath import sqrt
a=int(input())
b=int(input())
print(str(round(0.5*(math.tan(a/b)*(180/math.pi))))+'°')


# In[152]:


a=4
for i in range(1,a+1):
    for j in range(1,i+1):
         print(j,end='')
    for j in range(i-1,0,-1):
        (print(j,end=''))
    print('\a')

#1
#121
#12321
#1234321
        


# In[ ]:


print(pow(2,5))


# In[57]:


round(3.59)


# In[99]:


for i in range(4):
    print(i,end='')

