
# coding: utf-8

# In[139]:


# O-letter letter framing
a=5
for i in range(a):
    if(i%a):
        print('*','*'.rjust(3))
    if(i==0):
        print(a*'*')
    if(i==(a-1)):
        print(a*'*')
        


# In[120]:


print()

