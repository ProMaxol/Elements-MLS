#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problema 2 , definición de una función.

def div(n,m):
    if n > m & m > 0:
        return ((n-1)/m) + ((n-1)/(m-1))
    elif m == n:
        return 1 
    elif m == 0:
        return 1


    


# In[2]:


#Pruebas
print(div(50,35))
print(div(100,85))


# In[ ]:




