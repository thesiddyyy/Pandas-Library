#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('Pip install pandas')


# In[1]:


import pandas


# In[2]:


import pandas as pd


# # Creation of SERIES FROM SCALLER VALUE

# In[4]:


Series1=pd.Series([10,20,30])
print(Series1)


# In[7]:


Series2=pd.Series([10,20,30],index=['A','B','C'])
print(Series2)


# In[9]:


Series3=pd.Series([10,20,30,40,50,60],index=['A','B','C','D','E','F'])
print(Series3)


# # Creation of series from NUMPY ARRAY

# In[3]:


import numpy as np


# In[21]:


arr1=np.array([1,2,3,4])
Series5=pd.Series(arr1)
print(Series5)


# In[19]:


arr1=np.array([1,2,3,4])
Series5=pd.Series(arr1,index=['A','B','C','D'])
print(Series5)

# Creation of SERIES from DICTIONARY
# In[22]:


dict1={'India':'New Delhi','Uk':'London','Japan':'Tokyo'}
Series7=pd.Series(dict1)
print(Series7)


# # Access an element from series

# In[31]:


Series8=pd.Series([1,2,3,4,5],index=['A','B','C','D','E'])
print(Series8[['A','C','D']])


# In[4]:


import pandas as pd


# In[10]:


series4 = pd.Series([10,20,30,40,50])
print(series4[1:3])


# In[11]:


import numpy as np


# In[16]:


series5 = pd.Series(np.arange(10,16,1))
print(series5)


# In[31]:


series5 = pd.Series(np.arange(10,16,1),index=['a','b','c','d','e','f'])
series5[1:3] = 50
print(series5)


# # Mathematical Operation

# In[34]:


seriesA = pd.Series([40,50,60],index=['a','b','c'])
print(seriesA)


# In[35]:


seriesB = pd.Series([10,20,-50,-30],index=['x','y','b','c'])
print(seriesB)


# In[36]:


seriesA + seriesB


# In[37]:


seriesA - seriesB


# In[38]:


seriesA * seriesB


# In[39]:


seriesA / seriesB


# # Data Frame

# # A data frame is a two dimensional label data structure like a table of MYSQL.It contains rows and column.Each column have different type of values such as Numeric and String etc.

# In[56]:


data1 = {"Calories" : [400,500,600],"Duration" : [50,60,70]}
df = pd.DataFrame(data1,index = ['a','b','c'])
print(df)


# In[53]:


print(df.loc[[1,2]])


# # Creation of Data Frame from numpy ND array

# In[5]:


import numpy as np


# In[6]:


import pandas as pd


# In[10]:


arr1 = np.array([10,20,30])
arr2 = np.array([100,200,300])
arr3 = np.array([-10,-20,30,-40])
dframe = pd.DataFrame([arr1,arr2,arr3],columns = ['A','B','C','D'])
print(dframe)


# # Creation of DataFrame from list of Dictionary

# In[13]:


dict_list = [{'a':10,'b':20},{'a':30,'b':10,'c':40}]
df1 = pd.DataFrame(dict_list)
print(df1)


# # Creation of Data Frame from Dictonary of list

# In[14]:


list_dict = {'State':['Assam','Up','Mp'],'Zip Code':[99,88,77]}
df2 = pd.DataFrame(list_dict)
print(df2)


# In[ ]:





# In[15]:


Seriesa=pd.Series([10,20,30],index=('A','B','C'))
Seriesb=pd.Series([40,30,10],index=('D','E','F'))
df3=pd.DataFrame([Seriesa,Seriesb])
print(df3)


# # Create a Data Frame result sheet marks of 5 student in 3 subject.The name of student are the keys to dict and the index value of the series are the subject name

# In[21]:


Resultsheet = {'Sid':pd.Series([90,91,95],index = ['Python','sql','Stats']),
               'Ronit':pd.Series([90,88,98],index = ['Python','sql','Stats']),
                'Swara':pd.Series([88,97,77],index = ['Python','sql','Stats']),
                 'Khushi':pd.Series([55,89,99],index = ['Python','sql','Stats'])}
Rdf = pd.DataFrame(Resultsheet)
print(Rdf)


# # Adding new column.

# In[22]:


Rdf['Rishab']=[80,92,87]
print(Rdf)


# # Update the column

# In[25]:


Rdf['Ronit']=[70,88,98]
print(Rdf)


# # Access Data Frame element through indexing

# In[6]:


Rdf
Rdf.loc [['Science']]
Rdf.loc [: , 'A']
print()


# # Joining,merging and concatination of Data Frame

# In[10]:


dframe1 = pd.DataFrame([[1,2,3],[4,5],[6]],index = ['R1','R2','R3'], columns = ['C1','C2','C3'])
dframe2 = pd.DataFrame([[10,20],[30],[40,50]],columns = ['C2','C5'], index = ['R4','R2','R5'])


# In[17]:


print(dframe1)


# In[18]:


print(dframe2)


# In[24]:


dframe1 = dframe1._append(dframe2)
print(dframe1)


# # Attributes of Data Frame

# In[27]:


dframe1.index


# In[28]:


dframe1.columns


# In[29]:


dframe1.shape


# In[31]:


dframe1.size


# In[33]:


dframe1.head()


# In[34]:


dframe1.tail()


# # Cleaning empty cells 

# In[1]:


import pandas as pd 


# In[4]:


df = read.csv("C:\\Users\\Gratitude\\OneDrive\\Desktop\\Health_data.csv")


# In[1]:


new_df = df.dropna()
print(new_df.to_string())


# # Cleaning Wrong Data

# In[ ]:




