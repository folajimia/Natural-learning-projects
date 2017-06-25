Multiple Linear Regression
==========================

when an attempt is made to model the relationship between a dependent variable and two or more independent variables we refer to
this as multiple linear regression. This can be achieved by fitting a linear equation. Involving more independent variables creates
a more complicated model although it helps to get a better prediction. Adding more independent variables means that to visualize the 
model more dimensions will be involved.


y = M1X1 + M2X2 + b

with more independent variables, visualization become harder


Multiple Linear Regression Code
The code exercise here is from udacity. It uses the Boston house-prices dataset. The dataset consists of 13 features of 506 houses and 
their median value in $1000's. The code fits a model on the 13 features to predict on the value of houses.

It was solved with the following steps

1. Build a linear regression model
Create a regression model using scikit-learn's LinearRegression and assign it to model.
Fit the model to the data.

2. Predict using the model
Predict the value of sample_house.