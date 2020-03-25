#!/usr/bin/env python
# coding: utf-8

# ## Python’s Core Data Types:

# In[8]:


from IPython.display import Image
Image("Core_Data_Types.png")


# ### Numeric Types: 
# 
#     int
#     float
#     Decimal
#     Fraction

# ### Numeric literals and constructors
#     Literal                                       Interpretation
#     1234 , −24 , 0 , 99999999999999               Integers (unlimited size)
#     1.23 , 1. , 3.14e-10 , 4E210 , 4.0e+210       Floating-point numbers
#     0o177 , 0x9ff , 0b101010                      Octal, hex, and binary literals in 3.X
#     0177 , 0o177 , 0x9ff , 0b101010               Octal, octal, hex, and binary literals in 2.X
#     3+4j , 3.0+4.0j , 3J                          Complex number literals
#     set('spam'), {1, 2, 3, 4}                     Sets: 2.X and 3.X construction forms
#     Decimal('1.0'), Fraction(1, 3)                Decimal and fraction extension types
#     bool(X), True, False                          Boolean type and constants

# ### Mathematical Operations: 
# 
#     / division (always returns a float) 
#     //  integer divivision
#     %  remainder
#     **  calculates powers
#     =  assignment

# ## Numbers

# You can add (+), subtract (-), multiply (*), and divide (/) integers in Python.

# In[7]:


print(5 + 10)


# In[8]:


print(5 - 10)


# In[9]:


print(4 * 8)


# In[10]:


print(5 / 2)


# ### Power of ...

# In[5]:


print(2 ** 7)  # 2 to the power of 7


# In[11]:


print(5 ** 3)


# In[13]:


print(2 ** -2) # is equal to 1 / 4


# In[14]:


print((5 + 2) ** 2)


# ## Floats

# In[16]:


print(0.5 + 0.8)


# In[18]:


print(0.5 - 0.8)


# In[17]:


print(0.2 * 0.3)


# In[19]:


print(0.5 / 2)


# ### Mathematical Operators

# In[1]:


print(17 / 3)  # classic division returns a float


# In[21]:


print(17 // 3)


# In[3]:


print(17 % 3)  # the % operator returns the remainder of the division


# In[4]:


print(5 * 3 + 2) # operator precedence


# ## String

# In[22]:


print("String example")


# In[23]:


print('String example')


# In[24]:


print("Python is my 'favorite' language!")


# In[25]:


print('Python is my "favorite" language!')


# In[27]:


print('Python Course'.upper())


# In[28]:


print('Python Course'.lower())


# In[29]:


print('Python Course  '.rstrip()) # remove whitespace from the right side


# In[30]:


print('   Python Course'.lstrip()) # remove whitespace from the left side


# ### All String Functions

# In[31]:


print(dir('Python Course')) # The dir command lists all the functions that the data type has.


# ## Variables

# In[48]:


course_name = "Python Programming"
course_code = "BLM19250E"
nbrofStudent = 30


# In[49]:


print("Course Code: " + course_code + ", Course Name:" + course_name)


# In[ ]:


print("Course Code: " + course_code + ", Course Name:" + course_name + " Number of Students:" + nbrofStudent)


# In[54]:


print(f"Course Code: {course_code}, Course Name: {course_name}, Number of Students: {nbrofStudent}")


# In[59]:


width = 20
height = 5 * 9
area= width * height
print(f"The Field Area: {area}")


# In[61]:


birth_year = 2000
current_year = 2020
age = current_year - birth_year
name = "Mr. Nobody"
print(f"{name} age: {age}")


# ### Boolean Operations:
# 
#     and
#     or
#     not

# In[63]:


print(True and False)
print(True or False)
print(True and not False)


# In[70]:


condition_1 = True
condition_2 = False
print(condition_1 & condition_2)


# ### Comparisons:
# 
#     Operation	Meaning
#     
#         <	strictly less than
#         <=	less than or equal
#         >	strictly greater than
#         >=	greater than or equal
#         ==	equal
#         !=	not equal
#         is	object identity
#         is not	negated object identity

# In[56]:


print("3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)


# In[57]:


print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)


# In[ ]:




