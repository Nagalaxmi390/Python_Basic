
# coding: utf-8

# In[1]:


from collections import OrderedDict
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30


# In[50]:


from collections import OrderedDict
from collections import Counter
d={}
d=OrderedDict()
n=int(input())
f=[]
for i in range(n):
    a=input().split()
    f.append(int(a[-1]))
    d[" ".join(a[:len(a)-1])]=int(a[-1])
s=list(Counter(f).values())
t=list(d.items())
p=[]
for i in range(len(t)):
    p=list(t[i])
    print(p[0],s[i]*int(p[-1]))


# In[99]:


from collections import deque
d = deque()
n=int(input())
for i in range(n):
    x=input().split()
    if(x[0]=='append'):
        d.append(int(x[1]))
    if(x[0]=='appendleft'):
        d.appendleft(int(x[1]))
    if(x[0]=='pop'):
        d.pop()
    if(x[0]=='popleft'):
        d.popleft()
print(*d)


# In[95]:


6
append 1
append 2
append 3
appendleft 4
pop
popleft

