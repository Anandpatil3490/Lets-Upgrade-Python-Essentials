#!/usr/bin/env python
# coding: utf-8

# # Lists & its default functions

# In[1]:


lst = ['anand', 'g','Patil',12, 34.56, [1,2,3]]


# In[2]:


lst.append('karnataka')


# In[3]:


lst


# In[4]:


lst.clear()


# In[5]:


lst


# In[18]:


lst = ['anand', 'g','Patil',12, 34.56, [1,2,3]]


# In[19]:


lst


# In[20]:


a = lst.copy()


# In[21]:


a


# In[22]:


lst.count('anand')


# In[24]:


lst1 = ['munich','germany']


# In[25]:


lst.extend(lst1)


# In[26]:


lst


# In[28]:


lst.index([1, 2, 3])


# In[30]:


lst.insert(6, 'karnataka')


# In[31]:


lst


# In[32]:


lst.pop()


# In[41]:


lst


# In[42]:


lst.remove('karnataka')


# In[43]:


lst


# In[44]:


lst.reverse()


# In[45]:


lst


# In[46]:


b = [1,3,5,7,2,4,6,8]


# In[47]:


b.sort()


# In[48]:


b


# In[49]:


b.sort(reverse= True)


# In[50]:


b


# # Dictonary & its default functions

# In[51]:


dic = {'name':'anand', 'place':'munich','age':28}


# In[52]:


dic


# In[53]:


dic.clear()


# In[54]:


dic


# In[55]:


dic = {'name':'anand', 'place':'munich','age':28}


# In[56]:


d= dic.copy()


# In[57]:


d


# In[58]:


dic.get('name')


# In[67]:


name = ['ananad','shashi','sanjeev']
values= 'sport'
sports = dict.fromkeys (name,'sport')


# In[68]:


sports


# In[69]:


sports.keys()


# In[70]:


sports.values()


# In[71]:


sports.items()


# # Sets & its default functions

# In[73]:


sets= {'anand','quelle', 1, 2, 2, 45, 54, 45 }


# In[74]:


sets


# In[75]:


sets.clear()


# In[76]:


sets


# In[77]:


sets1= {'anand','quelle', 1, 2, 2, 45, 54, 45 }


# In[80]:


d = sets1.copy()


# In[81]:


d


# In[84]:


a = {'a', 'b', 'c', 'd'}
b = {'c','d', 'e'}
print (a.difference(b))
print (b.difference(a))


# In[85]:


a.intersection(b)


# In[87]:


print (a.difference_update(b))


# In[88]:


print (b.difference_update(a))


# In[89]:


a


# In[90]:


b


# In[93]:


A = {10,20,40,80}
B = {90, 80,10,100}
A.difference_update(B)
print (A)


# In[94]:


a.union(b)


# In[95]:


m= {1, 2, 4, 5}
n= {2,5}
n.issubset(m)


# # Tuple & its default functions 

# In[98]:


tup= (1,2,3,4,1,4)


# In[99]:


tup.count(1)


# In[100]:


tup.index(4)


# # Strings & its default functions

# In[102]:


name = 'anand'
surname= 'PATIL'
print(name.capitalize())


# In[103]:


surname.casefold()


# In[104]:


name = name.center(40)


# In[106]:


len(name)


# In[111]:


string = 'i am here, i am there'
substring = 'am'
coun = string.count(substring)
print("The count is:", coun)


# In[116]:


string.endswith ('am there')


# In[117]:


string.endswith('am There')


# In[ ]:


string.

