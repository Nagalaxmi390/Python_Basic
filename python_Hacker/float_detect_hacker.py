
# coding: utf-8

# In[38]:


def is_number(n):
    n=int(n)
    for i in range(n):
        s=input()
        if(s=='0'):
            print(False)
        else:
            try:
                float(s)
                print(True)
            except ValueError:
                print(False)
n=input()
is_number(n)


# In[33]:


5

1.414

+.5486468

0.5.0

1+1.0

0


# In[23]:


num=input()
print(isinstance(num, float))

