
# coding: utf-8

# In[ ]:


n=int(input())
for i in range(n):
    x=input()


# In[13]:


import re
xx="gu ru99,educatio0n is fun"
r1=re.findall(r"^\w+",xx)
print(r1)


# In[15]:


import re
xx = "guru99,education is fun"
r1 =re.findall(r"^\w+", xx)
print((re.split(r'\s','we are splitting the words')))
print((re.split(r's',' split the words')))


# In[20]:


import re
txt = "The rain in Spain"
x = re.match("^The.*Spain$", txt) 
print(x)


# In[25]:


import re
txt = "The rain in Spaina"
x = re.findall("a", txt)
print(x)


# In[26]:


import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x) 


# In[36]:


import re

txt = "Thenaga rain in Spain"
x = re.search("\s", txt)
print( x.end()) 


# In[40]:


import re
txt = "Thie rain in Spain"
x = re.search("\n", txt)
print(x) 


# In[48]:


import re

txt = "The rain in Spain"
x = re.split("\s", txt,5)
print(x) 


# In[51]:


import re

txt = "The rain in Spain"
x = re.sub("\ZSpain", "909", txt)
print(x) 


# In[52]:


import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x) 


# In[68]:


import re

txt = "The rain in Spain"
x = re.search("Spain\Z", txt)#end to end match in teh sentence
print(x)#ending and starting index of the searching charector


# In[59]:


import re
txt = "The rain in Spain"
x = re.search(r"i", txt)
print(x.string)


# In[65]:


import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) 


# In[73]:


import json#java script object notation

# some JSON:
x ='{"name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) 


# In[70]:


print(y)


# In[74]:


# a Python object (dict):
import json#loads and jumps
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y) 


# In[75]:


import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 


# In[76]:


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))


# In[83]:


try:
  print(l)
except ValueError:
  print("Something went wrong",ValueError)
finally:
  print("The 'try except' is finished") 


# In[85]:


try:
  print(s)
except NameError:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") 


# In[90]:


try:
      f=open("demofile.txt")
      f.write("Lorum Ipsum")
except:
      print("Something went wrong when writing to the file")


# In[100]:


x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed") 


# In[102]:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() 
class Student(Person):
    pass
p=Student("naga","laxmi")
p.printname()


# In[103]:


class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) 


# In[104]:


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019


# In[118]:


class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def naga(self):
        print(self.fname,self.lname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
x = Student("Mike", "Olsen", 2019) 
x.graduationyear


# In[113]:


print(x)

