#!/usr/bin/env python
# coding: utf-8

# ### Common list literals and operations
#     Operation                          Interpretation
#     L = []                             An empty list
#     L = [123, 'abc', 1.23, {}]         Four items: indexes 0..3
#     L = ['Bob', 40.0, ['dev', 'mgr']]  Nested sublists
#     L = list('spam')                   List of an iterable’s items, list of successive integers
#     L = list(range(-4, 4))
#     L[i]                               Index, index of index, slice, length
#     L[i][j]
#     L[i:j]
#     len(L)
#     L1 + L2                            Concatenate, repeat
#     L * 3
#     for x in L: print(x)               Iteration, membership
#     3 in L
#     L.append(4)                        Methods: growing
#     L.extend([5,6,7])                  L.insert(i, X)
#     L.index(X)                         Methods: searching
#     L.count(X)
#     L.sort()                           Methods: sorting, reversing,
#     L.reverse()                        
#     L.copy()
#     L.clear()
#     L.pop(i)                           Methods, statements: shrinking
#     L.remove(X)
#     del L[i]
#     del L[i:j]
#     L[i:j] = []
#     L[i] = 3                           Index assignment, slice assignment
#     L[i:j] = [4,5,6]
#     L = [x**2 for x in range(5)]       List comprehensions and maps
#     list(map(ord, 'spam'))s

# ### Create Basic List

# In[1]:


cities = ['Istanbul', 'Izmir', 'Ankara']
print(cities)


# In[2]:


mixList = ['Istanbul',34,'Izmir',35,'Ankara',6]
print(mixList)


# In[5]:


numberList = list(range(10))
print(numberList)


# In[6]:


characterList = list('Python Language')
print(characterList)


# ### Adding Elements to a List

# #### Appending Elements to the End of a List

# In[56]:


languages = ['Python', 'Java', 'C', 'C++']
languages.append('R')
print(languages)


# In[57]:


languages.append(['Rust', 'Dart'])
print(languages)


# In[58]:


# Alternative

languages[len(languages):] = ['PHP','Javascript']
print(languages)


# #### Extend Keyword

# In[38]:


languages = ['Python', 'Java', 'C', 'C++']
languages.append('R')
languages.extend(['Rust', 'Dart'])
print(languages)


# #### Inserting Elements into a List

# In[48]:


brands = ['Hyundai', 'Fiat']
brands.insert(0, 'Ford')
print(brands)


# In[49]:


brands.insert(1, ['Lexus', 'Nissan'])
print(brands)


# In[50]:


brands.insert(5, 'TOGG')
print(brands)


# ### Concatenate List

# In[39]:


L1 = ['A', 'B', 14]
L2 = ['C', 'D', 23]
print(L1 + L2)


# In[40]:


print(L1 * 3)


# ### Get Element Index

# In[60]:


courses = ['CSE611', 'CSE541', 'EENG143']
index = courses.index('CSE541')
print(index)


# ### The count of the given element

# In[61]:


animals = ['Cat', 'Dog', 'Lion', 'Elephant', 'Cat', 'Dog', 'Rat', 'Dog']
print(animals.count('Dog'))


# ### Sort The Element of the List

# In[62]:


C = [10,80,1,45,0]
C.sort()
print(C)


# In[64]:


C = [10,80,1,45,0]
print(sorted(C))
print(C)


# ### Reverse List

# In[65]:


C.reverse() # reverses the list
print(C)


# ### Removing Elements from a List

# In[73]:


mixedList = ['Istanbul', 34, 'Izmir', 35, 'Ankara', 6, 'Muğla', 48, 1, 2, 3, 'a', 'b', 'c']
mixedList.clear() # is equal to mixedList[:] = [] 
print(mixedList)


# In[74]:


mixedList = ['Istanbul', 34, 'Izmir', 35, 'Ankara', 6, 'Muğla', 48, 1, 2, 3, 'a', 'b', 'c']
mixedList.remove('Muğla')
print(mixedList)


# In[77]:


mixedList = ['Istanbul', 34, 'Izmir', 35, 'Ankara', 6, 'Muğla', 48, 1, 2, 3, 'a', 'b', 'c']
mixedList.pop() # remove Last Item
print(mixedList)


# In[78]:


mixedList.pop(1) # remove i^th index Item
print(mixedList)


# ### Using List in Loops

# In[ ]:


mixList = ['Istanbul',34,'Izmir',35,'Ankara',6]
for item in mixList:
    print(item)


# In[3]:


number_list = range(100, 1, -1)
for number in number_list:
    print(number)


# In[4]:


number_list = list(range(100, 1, -1))
print(number_list)


# In[6]:


power_of_numbers = []
for number in range(1, 11):
    power_of_numbers.append(number ** 2)

print(power_of_numbers)


# In[7]:


print("Min:", min(power_of_numbers))
print("Max:", max(power_of_numbers))
print("Sum:", sum(power_of_numbers))


# In[9]:


L = [i**2 for i in range(1, 11)]
print(L)


# ### Accessing Elements in a List

# In[15]:


mixList = ['Istanbul',34,'Izmir',35,'Ankara',6]

print(mixList[0])
print(mixList[-1])
print(mixList[len(mixList) - 1])


# In[10]:


print(mixList[0:5]) # Slicing


# In[25]:


"""
print(mixList[0::2])
print(mixList[0:-1:2])
print(mixList[:-1:2])
"""
print(mixList[::2])


# In[19]:


print(mixList[::-1])


# ### Copy The Elements of The List

# In[72]:


L1 = [50, 20, 40, 30, 20, 10]
copyL1 = L1.copy() # a new list instance is returned
print(copyL1)


# ### Tuple

# In[12]:


mixTuple = ('Istanbul',34,'Izmir',35,'Ankara',6)
for item in mixTuple:
    print(item)


# In[13]:


print(mixTuple[0])
print(mixTuple[0:3])


# ### Create Tuple with Compherension

# In[19]:


tuple(i for i in mixList)


# ### Bonus

# In[82]:


matrix = [[1, 2],
          [3, 4],
          [5, 6]]

sumofRow= [sum(row) for row in matris]
print(sumofList)


# In[83]:


squareMatrix = [[col ** 2 for col in row] for row in matris]


# In[84]:


print(squareMatrix)


# In[ ]:




