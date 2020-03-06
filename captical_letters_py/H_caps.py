
# coding: utf-8

# In[66]:


#H letter framing
a=6
for i in range(a):
    k=i*'*'
    p=(i-1)*'*'
    print(k.ljust(a),k.rjust(a))
for i in range(a,0,-1):
    k=i*'*'
    p=(i-1)*'*'
    print(k.ljust(a),k.rjust(a))

