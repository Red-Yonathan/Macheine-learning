import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# df = pd.read_csv('S_africa_export_data.csv')
# # df.columns=['Y','X']
# df.columns=['','Y','X']
# print(df.head())
# # print(df['X']) #also can be df.X and df.Y also works 
# print('trial: ',df.X) # is the same as df['X']
# # print("the trial",df.Y)
# # print(df.X.values)
# # print(df.X.values.shape) #-->  (120,)
# # print("neaxis: ", df.X.values[:])
# # print("neaxis: ", df.X.values[:,np.newaxis])
# # print("neaxis: ", df.X.values[:,np.newaxis].shape)
# x= df.X.values #-> flattenes the whole array into a 
# print(x, "values shape:", x.shape)
# print("------------------------------")
# print(x[:],"shape:", x[:].shape)
# print("------------------------------")
# print(x[:,np.newaxis], "newaxis shape:",x[:,np.newaxis].shape)
# print("------------------------------")

# a=np.array([[1,2,3,4,5,6,7]])
# print(a.sum())

# # print('index: ',len(df.index))
# # print(np.arange(10))
# # plt.plot(np.arange(len(df.Y)), df.Y) # Create a line plot for the ZAR/USD values
# # plt.title("ZAR/USD over time") # Title of the plot
# # plt.xlabel("Months") # Label for the x-axis 
# # plt.ylabel("ZAR/USD") # Label for the y-axis
# # plt.show() # Display the plot





############################################## My trainings-------------
# df = pd.read_csv('S_africa_export_data.csv')
# # df.columns=['Y','X']
# df.columns=['','Y','X']
# print(df.head())

# X= df.X.values  
# Y =  df.Y.values

# x_bar =  np.mean(X)
# y_bar = np.mean(Y)
# m = sum((df.X-x_bar)*(df.Y - y_bar))/ sum((df.X-x_bar)**2)
# print(m)

# a = y_bar - m*x_bar
# print("a:",a)
# y_gen = m*df.X + a
# print("y:",y_gen)

# # plt.title("Red's graph")
# # plt.scatter(X,Y)
# # plt.plot(X,y_gen,color="red")
# # plt.show()
# error =   Y - y_gen
# # error = (sum(Y-y_gen)**2)
# # error = np.round(error,11)
# print("*"*30)


# error2 = np.round(sum(error**2),11 )
# print("Error",error2)

df = pd.read_csv('S_africa_export_data.csv')
df.columns=['','Y','X']
lm = LinearRegression()
X = df.X.values[:,np.newaxis]
lm.fit(X,df.Y)
m= lm.coef_[0]
a= lm.intercept_

gen_y = lm.predict(X)

for i,x in enumerate(gen_y):
    print(x)

# error = ((gen_y-df.Y)**2).sum()  #but instead we can also do this 
# print("Error:",error)

print("error:", metrics.mean_squared_error(df.Y,gen_y))

print("m:",m,"a:",a)
print("*"*40)
plt.scatter(X,df.Y)
plt.plot(X,gen_y, color="red")
plt.show()

# print(df.X.values,df.X.values.shape)
# print("*"*40)
# print(df.X.values[:,np.newaxis],df.X.values[:,np.newaxis].shape)