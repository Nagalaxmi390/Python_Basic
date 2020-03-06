
# coding: utf-8

# In[69]:


#H letter framing
a=6
for i in range(a):
    k=i*'*'
    p=(i-1)*'*'
    print(k.rjust(a),k.ljust(a))
for i in range(a,0,-1):
    k=i*'*'
    p=(i-1)*'*'
    print(k.ljust(a),k.rjust(a))

