
# coding: utf-8

# In[23]:


# B-letter letter framing
a=5
for i in range(a):
    if(i%a):
        print('*'.ljust(round(round((a+1)/2))),'*'.rjust(round(round((a+1)/2))))
    if(i==0):
        print((a+1)*'*')
    if(i==round(a-1)/2):
        print((a+1)*'*')
    if(i==(a-1)):
        print((a+1)*'*')
        


# In[15]:


print()

