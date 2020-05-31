#!/usr/bin/env python
# coding: utf-8

# In[1]:


#task1
num = list(range(2000,3201))
req = []
for i in num:
    if i%7 == 0 and i % 5 != 0:
        req.append(i)

print(req,end="")


# In[2]:


first_name = input("enter your first name:")
last_name = input("enter your last name:")
print(last_name,first_name)


# In[ ]:


import math
dia = 12
radius = dia/2
volume = math.pi*(4/3)*(radius * radius * radius)
print(volume)


# In[ ]:


num =input('enter numbers seperated by comma').split(',')
print(num)


# In[8]:


l = input()
m = l[::-1]
print(m)


# In[ ]:


num = list(input('enter numbers seperated by comma'))
m = []
for i in num:
    if i == ',':
        continue
    m.append(i)
print(m)


# In[9]:


for j in range(0,6):
    print('*'*j)
    if j >4:
        for i in range(4,0,-1):
            print('*'*i)


# In[2]:


x = """WE, THE PEOPLE OF INDIA,
    having solemnly resolved to constitute India into a SOVEREIGN,!
        SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
         and to secure to all its citizens"""
print(x)


# In[3]:


y = "WE, THE PEOPLE OF INDIA,\n \thaving solemnly, resolved to constitute India into a SOVEREIGN,! \n \t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n \t \t and to secure to all its citizens"
print(y)


# In[ ]:




