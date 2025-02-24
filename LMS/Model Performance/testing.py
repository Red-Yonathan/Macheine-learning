import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("regression_sprint_data_1.csv")

df.columns=['','Y','X']


print(df.head())
print("*"*50)
X= df.drop(['Y',''],axis=1) # so basically we are droping  the Y column from our dataframe so that X == df.X ...
                        #... axis =1 means column and axis =0 means row. so ('Y',axis=1) means find 'Y' from column and drop it

                        # when droped X will be a (120,2) array. and df.X will be (120,1) array.
# print(X.shape) # ->(120,1)



y =df['Y'] # and not df.Y beacuse df.y is just one dimentional list
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=50)

# plt.scatter(x_test,y_test,color ='red')
# plt.scatter(x_train,y_train, color ="darkblue")
# plt.show()

lm = LinearRegression()

lm.fit(x_train,y_train)
a= lm.intercept_
m = lm.coef_[0]
gen_y = lm.predict(x_train)

# plt.scatter(x_train,y_train,color="darkblue")
# plt.scatter(x_train,gen_y,color="red",edgecolors="green")
# plt.show()

gen_y_test = lm.predict(x_test)

plt.scatter(x_test,y_test,color = "darkblue")
plt.scatter(x_test,gen_y_test,color ="red",edgecolors="green")
plt.show()

from sklearn import metrics

print(f"MSE: {metrics.mean_squared_error(y_test,gen_y_test)}")