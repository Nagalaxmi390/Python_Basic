
# coding: utf-8

# In[92]:


#class is a blue print for the creating objects or a object constructor
class person:
  def __init__(Self, name,age):
    Self.name =name
    Self.age = age
    if(name=='John'):
        print('nothinf')
p1 = person("John", 10)
print(p1.name)
print(p1.age)


# In[97]:


class Person:
    def __init__(self,name):
        self.name=name
    def naga(self):
        print("my name is:"+self.name)
p1=Person("Naga")
p1.naga()


# In[74]:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 


# In[76]:




