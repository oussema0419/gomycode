#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

DFExam = pd.DataFrame(exam_data, index=labels)
print(DFExam)

DFExam.head(3)

DFExam = DFExam.drop(['d', 'h'])
print(DFExam)

print(DFExam[["name","score"]])

dict2 = {"name": ["Suresh"], "score": [15.5], "attempts": [1], "qualify": ["yes"], "labels": ["k"]}
DF2 = pd.DataFrame(dict2)
DF2 = DF2.set_index("labels")
DFExam = pd.concat([DFExam,DF2])
print(DFExam)

DFExam = DFExam.drop(['attempts'], axis=1)
print(DFExam)
labels = ['a', 'b', 'c', 'e', 'f', 'g', 'i', 'j','k']
Dict3={"success":[]}
DF3 = pd.DataFrame(Dict3)
for x in labels:
    if DFExam.loc[x]["qualify"]=='yes':
        DF3.loc[x] = 1
    else:
        DF3.loc[x] = 0
DFExam["success"] = DF3
print(DFExam)

#DFExam.to_csv('checkpoint7.csv')
#new_data = pd.read_csv('checkpoint7.csv')
#new_data.head(9)


# In[ ]:




