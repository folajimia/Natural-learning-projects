from sklearn.linear_model import LinearRegression

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np


# assign the dataframe to this variable
#load data
challangeSet = pd.read_csv('challage_dataset.csv')






x_values = challangeSet[['x']]   #.values.reshape(-1, 1)

y_values = challangeSet[['y']]


#train model on data
challangeSet = LinearRegression()
challangeSet.fit(x_values, y_values)


#7.5402	6.7504



#Make a prediction using the model
y_prediction = challangeSet.predict(7.5402)

print(y_prediction)

#error btw actual and predicted x_values

error = 6.7504 - y_prediction

#TODO
#replace 6.70504 with computer picked random value




print("Error: %.2f" % error)


# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((challangeSet.predict(x_values) - y_values) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % challangeSet.score(x_values, y_values))

#visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, challangeSet.predict(x_values))
plt.show()




