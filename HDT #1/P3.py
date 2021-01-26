#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problema 3 , impresión de un rombo.

def rombo(num):
    for i in range(1, num+1):
      i = i - (num//2 +1)
      if i < 0:
        i = -i
      print(" " * i + "*" * (num - i*2) + " "*i)


# In[7]:


rombo(3)
print()
rombo(5)
print()
rombo(7)
print()
rombo(9)


# In[ ]:




