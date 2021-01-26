#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Problema 3 , impresión de un traingulo invertido.
def ti(n):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ', end='')
        for j in range(2*i-1):
            print('*',end='')
        print() 


# In[7]:


ti(4)
ti(5)
ti(6)

