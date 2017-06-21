Regression model

Linear regression is a method for modelling the relationship between a dependent variable and an independent one. In maths, dependent variables are usually represented with Y and the independent with X.
Linear regression is used to find out what relationship exists between all sorts of data.
Once a relationship has been established, it can be used to predict. For example, one might want to relate the weights to the height of a set of people. This relationship can then be used predict future heights from weights. 

If there appears to be no relationship between the independent and dependent variables, trying to fit a linear regression model to the data will probably not result in a useful model.
The numerical measure of association between two variables is called the correlation coefficient. The correlation coefficient usually falls between -1 and 1.
The equation  Y = a + bX  represents linear regression line where X is the independent variable and Y is the dependent variable. The slope of the regression line is b and a is the intercept.



In this code, I used linear regression to predict life expectancy from body mass index. The tool used is described below.
i.	For the linear regression model, be using scikit-learn's LinearRegression class. The function Fit() is provided in the class to fit the model to the data.
Below is an example where the variable prototype is a linear regression model that has been fitted to the data x_values and y_values. What it means to fit a model is finding the best line that fits the relationship between the two variables.

>>> from sklearn.linear_model import LinearRegression
>>> prototype = LinearRegression()
>>> prototype.fit(x_values, y_values)


To make a predictions using the model's predict() function.
>>> print(model.predict([127]))
[438.94308857]

The model returned a prediction for each input array. The input, [127], got a prediction of 438.94308857. The reason for predicting on an array like [127] and not just 127, is because you can have a model that makes a prediction using multiple features. 
Linear Regression code
In this code with solves an udacity problem, I’ll be using data obtained from Gapminder. The data is that of average life expectancy at birth and the average BMI for males across the world. 
The data is found in the file "bmi_and_life_expectancy.csv”. It includes three columns, containing the following data:
•	Country – The country a person is born in. 
•	Life expectancy – The average life expectancy at birth for a person in that country.
•	BMI – The mean BMI of males in that country.

The linear regression problem is solved in the following steps

1. Load the data
•	The data is in the file called "bmi_and_life_expectancy.csv".
•	Use pandas read_csv to load the data into a dataframe.
•	Assign the dataframe to the variable bmi_life_data.
2. Build a linear regression model
•	Create a regression model using scikit-learn's LinearRegression and assign it to bmi_life_model.
•	Fit the model to the data.
3. Predict using the model
Predict using a BMI of 21.07931 and assign it to the variable laos_life_exp.