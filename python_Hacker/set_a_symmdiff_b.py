
# coding: utf-8

# In[66]:


9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8


# In[72]:


#a but not b,set manipulations symmetrical difference
a=int(input())
x=set(map(int,input().split()[:a]))
n=int(input())
y=set(map(int,input().split()[:n]))
m=x^y
print(len(m))


# In[62]:


a

