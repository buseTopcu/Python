#!/usr/bin/env python
# coding: utf-8

# ### Dictionaries

# In[1]:


# A pair of braces creates an empty dictionary: {}
d = {}

print('d:', d)
print('type:', type(d))


# In[2]:


# The main operations on a dictionary are storing a value with 
# some key and extracting the value given the key
d = {'Name': 'Say my name', 'Age': 7};

d['Class'] = 'First'  # Add new entry

print('d:', d)
print("d['Name']:", d['Name'])


# ### Access Dictionary Items

# In[4]:


car = {"Brand": "Honda", "Model": "Civic", "Year": 2018, "Kilometer": 5e4}
print("Brand:", car['Brand'], "\nModel:", car['Model'], "\nYear:", car["Year"], "\nKilometer:", car['Kilometer'])


# ### Modify Dictionary Items

# In[5]:


car['Kilometer'] = 10e4
print(car)


# ### Starting with an Empty Dictionary

# In[10]:


person = {}
person['name'] = "Ahmet"
person['surname'] = 'Yılmaz'
person['age'] = 20
print(person)


# ### Removing Key-Value Pairs

# In[11]:


person['fullName'] = person['name'] + ' ' + person['surname']

del person['name']
del person['surname']
print(person)


# ### Access Dictionary Key, Value and Key-Value Pairs

# In[12]:


favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

print("Dictionary Keys:", favorite_languages.keys())
print("Dictionary Values:", favorite_languages.values())
print("Dictionray Key-Value Pairs:", favorite_languages.items())


# ### Looping Through All Key-Value Pairs

# In[15]:


course_teachers = {
    'CS411': 'Andrew NG',
    'CS325': 'Geoffrey Hinton',
    'CS124': 'Yan LeCun',
}

for course, teacher in course_teachers.items():
    print(f"{course}'s teacher is {teacher}")


# ### Looping Through a Dictionary’s Keys in Order

# In[18]:


for course  in sorted(course_teachers.keys()):
    print(f"{course}'s teacher is {course_teachers[course]}")


# ### A List of Dictionaries

# In[21]:


rental_cars = [
        {"Brand": "Honda", "Model": "Civic", "Year": 2018, "Kilometer": 5e4},
        {"Brand": "Renault", "Model": "Clio", "Year": 2019, "Kilometer": 1e3},
        {"Brand": "Fiat", "Model": "Egea", "Year": 2017, "Kilometer": 8e3},
        {"Brand": "Ford", "Model": "Focus", "Year": 2016, "Kilometer": 5e4},
      ]

print("Rental Car Lists:")
for car in rental_cars:
    print(car)


# In[22]:


import random as rnd
points = []

# Fill List
for i in range(5):
    points.append({"x": rnd.random(), "y": rnd.random()})

print("Random Points:")
for point in points:
    print(point)


# ### Dictionary Compherension

# In[23]:


square = {x: x ** 2 for x in (2, 4, 6)}

print('square:', square)


# In[27]:


print({x: [i**2 for i in range(x)] for x in range(1, 7)})


# ### Alternative Methods for Creating Dictionary

# In[29]:


a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])

isEqual = a == b == c == d

print(isEqual)  # True


# In[31]:


dict1 = {'one': 1, 'two': 2, 'three': 10}
dict2 = {'three': 3, 'four': 4, 'five': 5}

dict1.update(dict2)

print('dict1:', dict1)


# In[34]:


counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


# In[36]:


person = {'name': "Ayşe"}
print(person['name'])
print(person['age'])


# In[37]:


# Simple get method, with and without default value
person.setdefault('age', 15)
print(person['age'])


# In[35]:


counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1

print(counts)


# In[39]:


import random as rnd
user_basket = [{"username":"zkus"}, {'username':'anonymous'}]
items = ['Mobile Phone', 'Laptop', 'PC', 'Smart Watch']

for user in user_basket:
    user.setdefault('basket', []).append(rnd.choice(items))

print(user_basket)


# In[ ]:




