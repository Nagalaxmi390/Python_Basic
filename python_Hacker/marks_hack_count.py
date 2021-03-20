
# coding: utf-8

# In[1]:


x= 0;k = int(input())
m = input().strip().split()
for i in range(k): x = x+int(input().split()[m.index('MARKS')])
print(float(x)/k)# Enter your code here. Read input from STDIN. Print output to STDOUT


# In[3]:


m.index('C')

