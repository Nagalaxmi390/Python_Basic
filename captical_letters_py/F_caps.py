
# coding: utf-8

# In[13]:


# F-letter letter framing
a=5
for i in range(a):
    if(i%a):
        print('*'.ljust(round(round((a+1)/2))))
    if(i==0):
        print(a*'*')
    if(i==round(a-1)/2):
        print(a*'*')
        


# In[7]:


print()

