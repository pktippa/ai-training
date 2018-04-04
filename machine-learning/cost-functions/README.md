# Cost functions

## Cross Entropy

Hy'(y) = - sigsum(i, y'i * log(yi))

Where y is predicted probability distribution, y' is the true distribution(Ex: the one-hot encoded vector)
.More can be read [here](https://colah.github.io/posts/2015-09-Visual-Information)

## Gradient Descent

Shifts each variable a little bit in the direction that reduces the cost.

## Others

* [Logistic Regression Cost Function](log_reg_cf.md)