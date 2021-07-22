#!/usr/bin/env python
# coding: utf-8

# In[102]:


import numpy as np
a=np.array([1,2,3,4,5,6[1,2,3,4,5,6,7,8,9])
a=a.tolist()
print(type(a))
print(a)


# In[45]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
x=(a[0:1,1])+(a[1:,0])
print("manuellement :")
print(int(x))



#2eme methode :
n_array = np.array([[55, 25, 15],[30, 44, 2],[11, 45, 77]])
print("auto:")

trace = np.trace(n_array)

print(trace)


# In[123]:


import numpy as np
a=np.array([[1,29,3],[10,2,6]])
for i in range ((len(a)+1)):
    if (a[0:1,i])>3:
        print(a[0:1,i])
    elif (a[1:2,i])>3:
        print(a[1:2,i])


# In[124]:


import numpy as np
X = np.random.rand(5, 10)
print(X)
Y = X - X.mean(axis=1, keepdims=True)
print(Y)


# In[ ]:




