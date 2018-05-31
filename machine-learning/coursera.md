# Coursera Machine Learning - Standford

In Separate Project: Find [here](https://github.com/pktippa/datasciencecoursera)

* Linear Regression with One Variable or Univariate linear Regression.
* Hypothesis (h) is for mapping x's to y's 

To approach a problem for Linear regression, take few values of theta and try to plot same on the data points with line and see how the line cuts through the data.

Idea: Choose theta0, theta1 so that h(x) is close to y for our training example (x, y).

h_theta(x) = theta0 + theta1 * x

Cost Function or Squared Error Function or Mean Squared Error

J(theta0, theta1) = 1/2m(Sigma[i - 1 to m](h_theta(x)(i) - y(i)))^2

Optimization objective is to minimize the Cost Function

Try putting the constants in equation to zero in h_theta(x) = theta0 + theta1 * x

Lets say theta0 = 0, for various values of theta1, try to plot h_theta(x) and J(theta)

J(theta) will be a U shaped Parabola, having lowest point when theta1 = 1.
Why?

since theta0 = 0, h_theta(x) = theta1 * x;
if theta1 = 1 -> h_theta(x) = x

to have minimum value of Cost Function J -> 0 -> we need h_theta(x) = y, so the difference between them would be zero.

Contour Plots:

Converting the 3D plot to 2D plot by showing in ellipses.