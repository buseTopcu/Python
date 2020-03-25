#!/usr/bin/env python
# coding: utf-8

# In[2]:


name = input('What is your name:')
print(f"Hello {name}!")


# In[4]:


print("Creating Range...")
start = int(input("Enter the start value:"))
end = int(input("Enter the end value:"))
print(list(range(start, end + 1)))


# In[4]:


brand_list = ['Honda', 'Fiat', 'Ford', 'Hyundai', '']
counter = 0
while brand_list[counter] != '':
    print(brand_list[counter])
    counter = counter + 1


# In[10]:


import random as rnd
random_number = rnd.randint(1, 100)
prediction = 0

while prediction != random_number:
    prediction = int(input("Enter New Number:"))
    if prediction < random_number:
        print("Target Number greater than your prediction.")
    elif prediction > random_number:
        print("Target Number lower than your prediction.")

print("Congrats! You found correct answer.")


# In[16]:


number = int(input("Enter New Number:"))
isPrime = True
counter = 2

while counter < number:
    if number % counter == 0:
        isPrime = False
        break
    counter = counter + 1

print(f"Is {number} prime: {isPrime}")


# In[19]:


end = int(input("Enter the end value:"))
counter = 1

while counter < end:
    if counter % 3 == 0:
        counter = counter + 1
        continue
        
    print(counter)
    counter = counter + 1


# In[20]:


users = [("John", 1995), ("Anna", 2013), ("Bruce", 2011), ('Mary', 2000)]
accepted_users = []

while users:
    username, year = users.pop()
    age = 2020 - year
    if age > 18:
        accepted_users.append((username, age))

print(accepted_users)


# ### Extra

# In[13]:


number_list = [(3,5,7), (9,12), (15,17,19,21)]
print(f"Sum of All Elements: {sum(sum(a) for a in number_list)}")
print([sum(_list) for _list in number_list])


# In[ ]:




