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

Gradient Descent:

alpha - learning rate.

Simultaneous updates

temp0 := theta0 - d(J(theta0, theta1))/d(theta0)
temp1 := theta1 - d(J(theta0, theta1))/d(theta1)

theta0 := temp0
theta1 := temp1

The way we do this is by taking the derivative (the tangential line to a function) of our cost function. The slope of the tangent is the derivative at that point and it will give us a direction to move towards.

https://www.cliffsnotes.com/study-guides/calculus/calculus/applications-of-the-derivative/tangent-and-normal-lines

Negative slope and positive slope of a line can be found by looking at the line direction, like as x increases, does y increase or not.

The cost function for linear regression is always a bowl shaped or convex shaped function.

So it always has a global optimum but not a local optimum.

Using all the training examples to calculate new values of parameters(Ex: theta0, theta1) is called Batch Gradient Descent.

A vector is a special matrix with only one column!

For showing in form of matrices, the hypothesis parameters are formed in vector.i.e
[ theta0 ]
[ theta1 ]

it is a 2 dimensional vector .ie. 2 x 1 matrix

Matrix dont have a inverse is called "singular" or "degenerative"

A non square matrix does not have an inverse matrix

In matrix notations, the parameters are in n-dimensional vector.

so hypothesis becomes

h_theta(x) = theta(Transpose) * X

where

X =

X0
X1
X2

theta = 

theta0
theta1
theta2

n+1 dimensional vectors

and
theta(Transpose) = [theta0 theta1 theta2] ; row vector

h_theta(x) will get a real number.

remember X1, X2, X3 are always feature vectors

TODO - need visually
Actually the original data table if you visualize it will be transposed for all features

x(i)j = value of feature j in the ith training example
x(i) =the input (features) of the ith training example
m=the number of training examples
n=the number of features

Linear regression with multiple variables is also known as "multivariate linear regression".

See imgs\linear_regression_with_multiple_variables.PNG

Some times the multivariate linear regression may not work with look at the data
So choose the polynomial regression with features as x^2, x^3,sqrt(x).
Make sure you do the feature scaling.

there are algorithms to get to know which features to use for building the algorithm.

## Automatically finding the parameters - theta

We can use normal equation method, as the Cost function J is a quadratic function of theta(if there is only one parameter).

So to minimize any function we need to take derivative of the function and make it equal to zero. i.e d(J(theta))/dtheta = 0

Similarly for multiple theta parameters theta0, theta1, theta2 - take corresponding partial derivate and make it equal to 0

Normal Equation method 

theta = (X`X)^-1 * (X`)* y, where X` is X transpose

The cost of calculating inverse for n dimensions is O(n^3)

Normal equation method does not fit for Classification problems, it is more suitable for linear equation with number of features >= 10,000