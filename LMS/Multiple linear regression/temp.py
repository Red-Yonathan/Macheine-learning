# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#from sklearn.linear_model import LinearRegression
#import pandas as pd
#lm = LinearRegression()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
lm = LinearRegression()

#read the dataset

df = pd.read_csv('mtcars.csv', index_col=0)
df.head()


## create figure and 3d axes
#fig = plt.figure(figsize=(8,7))
#ax = fig.add_subplot(111, projection='3d')

## set axis labels
#ax.set_zlabel('MPG')
#ax.set_xlabel('No. of Cylinders')
#ax.set_ylabel('Weight (1000 lbs)')

## scatter plot with response variable and 2 predictors
#ax.scatter(df['cyl'], df['wt'], df['mpg'])

X = df.drop(['mpg'],axis =1)
y=df['mpg']
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)

lm.fit(x_train,y_train)

gen_y = lm.predict(x_test)
print(lm.score(X, y))


fig, axs = plt.subplots(2, 2, figsize=(9,7))

axs[0,0].scatter(df['wt'], df['mpg'])
axs[0,0].plot(df['wt'], lm.intercept_ + lm.coef_[4]*df['wt'], color='red')
axs[0,0].title.set_text('Weight (wt) vs. mpg')

axs[0,1].scatter(df['disp'], df['mpg'])
axs[0,1].plot(df['disp'], lm.intercept_ + lm.coef_[1]*df['disp'], color='red')
axs[0,1].title.set_text('Engine displacement (disp) vs. mpg')

axs[1,0].scatter(df['cyl'], df['mpg'])
axs[1,0].plot(df['cyl'], lm.intercept_ + lm.coef_[0]*df['cyl'], color='red')
axs[1,0].title.set_text('Number of cylinders (cyl) vs. mpg')

axs[1,1].scatter(df['hp'], df['mpg'])
axs[1,1].plot(df['hp'], lm.intercept_ + lm.coef_[2]*df['hp'], color='red')
axs[1,1].title.set_text('Horsepower (hp) vs. mpg')

fig.tight_layout(pad=3.0)

plt.show()