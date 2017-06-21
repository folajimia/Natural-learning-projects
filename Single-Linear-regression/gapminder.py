
import pandas as pd

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

# assign the dataframe to this variable
#load data
bmi_life_data = pd.read_csv('bmi_and_life_expectancy.csv')
print (bmi_life_data)

#for key in bmi_life_data:
#    print ("Key=" + key)

x_values = bmi_life_data['BMI'].values.reshape(-1, 1)

y_values = bmi_life_data['Life expectancy']


#Make and fit the linear regression model
bmi_life_model = LinearRegression()
bmi_life_model.fit(x_values, y_values)
bmi_life_model.fit(bmi_life_data[['BMI']], bmi_life_data[['Life expectancy']])


#Make a prediction using the model
laos_life_exp = bmi_life_model.predict(21.07931)

print(laos_life_exp)


#Plot the Life expectancy vs BMI
plt.plot(y_values, x_values, 'ro')
plt.ylabel('Life expectancy')
plt.xlabel('BMI')
plt.show()


