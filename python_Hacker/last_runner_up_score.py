
# coding: utf-8

# In[8]:



s=[(37.21,'Harry'),(37.21,'Berry'),(37.2,'Tina'),(41,'Akriti'),(39,'Harsh')]
s.sort()
b=[]
c=[]
a=[]
k=[]
for i in range(len(s)):
        b.append(s[i][0])
for i in range(len(b)):
    if(b[i] not in a):
        a.append(b[i])
        c.append(b.count(b[i]))
#print(a,c)
#print(a[1])
for i in range(len(s)):
    if(a[1]==s[i][0]):
            print(s[i][1])


# In[10]:


m=[]
n=[]
c=[]
b=[]
a=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        n.append(score)
        m.append(name)
s=list(zip(n,m))
s.sort()
#s=[(37.21,'Harry'),(37.21,'Berry'),(37.2,'Tina'),(41,'Akriti'),(39,'Harsh')]
s.sort()
for i in range(len(s)):
        b.append(s[i][0])
for i in range(len(b)):
    if(b[i] not in a):
        a.append(b[i])
        c.append(b.count(b[i]))
#print(a,c)
#print(a[1])
for i in range(len(s)):
    if(a[1]==s[i][0]):
            print(s[i][1])

