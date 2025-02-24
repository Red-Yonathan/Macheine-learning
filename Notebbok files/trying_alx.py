# class Tree:
#     def __init__(self, species, age, height):
#         self.species = species
#         self.age = age
#         self.height = height
#     def grow(self):
#         self.height +=1
#     def reseed(self):
#         print (f" the {self.species} tree disperses seeds")
    
#     def used_for(self): # this is an exmple for abstraction to be filled later
#         pass


# class Oak(Tree):
#     def budding(self):
#         print( f"this {self.species} is budding new leaves ")
# class Pine(Tree):
#     def cone_count(self):
#         print("this is a pine tree object")
# oak_tree = Oak('Oak',50,100)
# pine_tree = Pine("pine", 45,67)
# oak_tree.budding()
# if isinstance(oak_tree,Oak) :
#     oak_tree.budding()
# #this is what we call polymorphism
# for i in (oak_tree,pine_tree):
#     i.grow()
#     i.reseed()
#     if isinstance(i,Oak): # isinstance takes(object,class)
#         i.budding
#     if isinstance(i,Pine):
#         i.cone_count()

# #Abstraction 
# class work(Tree):
#     def __init__(self,species,age,height,type):
#         super().__init__(species,age,height)   
#         self.type =type
#     def used_for(self):
#         print(f"this tree is used for {self.type}")     

# a= work("Olive",170,20,'furniture')
# a.used_for()




## ----------------reversing a string --------------------
# def r(s):
#     if len(s) == 0:
#         return s
#     else:
#         return r(s[1:]) + s[0]

# print(r("you"))


# # f = list(filter(lambda x: x>2,[1,2,3,4,5]))
# # print(f)
# a= "o"
# print(a[2:])
#---------Numpy --------------
# import numpy as np

# a =  np.array([ [1,2,3],[4,5,6],[6,7,8] ]) # don't forget the double [[]]
# [[1 2 3]
#  [4 5 6]
#  [6 7 8]]


# print(a[a<5])
# print(a.shape)
# b= np.append(a,[[3,7,0]],axis=0)
# print(b)
# print(a[:,0])
# print(list(a[a<6]))
# b= np.append(a,[[6,7,8]],axis =1)
# print(a.sum(axis =0))
# print(a.sum(axis=1))
# b= a.sum(axis=1)
# print(b.shape)
# print(np.argmin(a,axis=1))
# print(np.argmax(a.mean(axis =1)))


#___________________________________________Pandas

import pandas as pd

# list_df = [[32, 'Portugal', 94], [30, 'Argentina', 93], [25 , 'Brazil', 92]]
list_df = {'age':[32,30,25], 'country':['portugal','Argentina', 'Brazil'],'score':[94,93,92]}
index =['abebe','kebede','bekele']
columns = ['age','country','scores']
# print(pd.DataFrame(data = list_df,columns = columns, index = index))
# print(pd.DataFrame(data = list_df,index = index))
# all =  pd.DataFrame(data = list_df,index = index, columns= columns)
df =pd.DataFrame(data =list_df, index = index)
print("original table \n", df)
print("--------------")
# print(df.iloc[0])
# print(df.loc["abebe"]) - use loc to find by name
# print(df.columns) ---- to get all the columns
# print(df.index) ---- to get all the rows

# print(df.iloc[0:2]) --- to get the first
# print(df['age'])  ---- to get columns
# print(df[['age','country']]) # double [[]] for multiple entries
# print(df.loc[['abebe','kebede']][['age','country']])

# print(df.iloc[0:2][['age','country']])
print(df[['age','country']].iloc[0:2])