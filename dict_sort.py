
# coding: utf-8

# In[66]:


x ={'q':1, 'w':2, 'e':3, 'r':4, 't':5, 'y':6}  
z=sorted(x)
a=list(x.keys())
y={}
for i in range(len(x)):
    if(z[i] in a):
        y[z[i]]=x[z[i]]
print(y)


# In[67]:


z


# In[62]:


a

