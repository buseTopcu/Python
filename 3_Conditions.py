#!/usr/bin/env python
# coding: utf-8

# ### If - Else Statements

# In[1]:


number_1 = 15
number_2 = 25

if number_1 > number_2:
    print("Number_1 greater than Number_2")
elif number_1 == number_2:
    print("Number_1 is equal to Number_2")
else:
    print('Number_1 lower than Number_2')
    


# In[3]:


grade = 76

if grade > 90:
    print("AA")
elif grade < 90 and grade >= 85:
    print("BA")
elif grade < 85 and grade >= 75:
    print("BB")
elif grade < 75 and grade >= 65:
    print("CB")
elif grade < 65 and grade >= 50:
    print("CC")
else:
    print("FF")


# In[5]:


username = 'admin'
password = 'admin123'

if username == 'admin':
    if password == 'admin123':
        print("Login Successfull!")
    elif password != 'admin123':
        print("Wrong Password")
else:
    print("Wrong Username")


# In[8]:


fruits = ['apple', 'grapes', 'strawberry', 'banana']

print("strawberry" in fruits)
print("strawberry" not in fruits)


# ### Ternary Operator

# In[11]:


result = True if 'orange' in fruits else False
print(result)


# In[13]:


n1 = 25
n2 = 12
_max = n1 if n1 > n2 else n2
print(_max)


# In[14]:


stockList = ['Mobile Phone', 'Laptop', 'Printer', 'Game Console']
basket = []

if 'Mobile Phone' in stockList:
    basket.append('Mobile Phone')
    print('Mobile Phone added to your basket')
if 'Laptop' in stockList:
    basket.append('Laptop')
    print('Laptop added to your basket')

print("Your Basket:", basket)


# In[16]:


basket = [item for item in stockList if item == 'Mobile Phone' or item == 'Laptop']
print(basket)


# In[22]:


results = ['Python Dictionary', 'Python dictionary parameters', 'How to use dictionary in python', 'java data types']
key = 'Python Dictionary'.lower()

for result in results:
    if key in result.lower():
        print('Search Result:', result)
    elif key.split(' ')[0].lower() in result.lower():
        print('Search Result:', result)
    elif key.split(' ')[1].lower() in result.lower():
        print('Search Result:', result)


# In[17]:


print([i**3 if i % 2 == 0 else i for i in range(20)])


# In[ ]:




