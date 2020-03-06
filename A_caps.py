
# coding: utf-8

# In[41]:


# A-letter letter framing
a=5
for i in range(a):
    if(i%a):
        print('*'.ljust(round(round((a+1)/2))),'*'.rjust(round(round((a+1)/2))))
    if(i==0):
        print((a+2)*'*')
    if(i==round(a-1)/2):
        print((a+2)*'*')
        


# In[28]:


print()

