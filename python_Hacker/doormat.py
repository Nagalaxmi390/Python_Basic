
# coding: utf-8

# In[47]:


N,M=map(int,raw_input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in xrange(0,N/2): 
    print('.|.'*i).rjust((M-2)/2,'-')+'.|.'+('.|.'*i).ljust((M-2)/2,'-')
print('WELCOME'.center(M,'-'))
for i in reversed(xrange(0,N/2)): 
    print('.|.'*i).rjust((M-2)/2,'-')+'.|.'+('.|.'*i).ljust((M-2)/2,'-')


# In[45]:


5

1.414

+.5486468

0.5.0

1+1.0

0


# In[23]:


num=input()
print(isinstance(num, float))

