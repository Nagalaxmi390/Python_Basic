
# coding: utf-8

# In[66]:


9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8


# In[73]:


def score_words(words):
    b=['a','e','i','o','u','y']
    c=0
    for i in range(len(words)):
        s=[]
        for j in range(len(words[i])):
            if(words[i][j] in b):
                s.append(words[i][j])
        if(len(s)%2==0):
            c=c+2
        else:
            c=c+1
        s.clear()
    return c

n = int(input())
words = input().split()
print(score_words(words))


# In[74]:


words


# In[76]:




