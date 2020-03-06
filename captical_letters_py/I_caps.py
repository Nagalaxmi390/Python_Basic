
# coding: utf-8

# In[149]:


# I-letter letter framing
a=5
for i in range(a):
    if(i%a):
        print('*'.rjust(round(round((a+1)/2))))
    if(i==0):
        print(a*'*')
    if(i==(a-1)):
        print(a*'*')
        


# In[120]:


print()

