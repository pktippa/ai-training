# Deep Learning by Google

[Course link](https://in.udacity.com/course/deep-learning--ud730)

## Quizes

1. [Softmax](https://classroom.udacity.com/courses/ud730/lessons/6370362152/concepts/63815621490923) - [Code](softmax.py)
2. [Numerical Stability](https://classroom.udacity.com/courses/ud730/lessons/6370362152/concepts/71235296110923) - [Code](numerical_stability.py)

## Notes
* Softmax function which converts classified labels scores into probabilities. Softmax Function S(yi) = exp(yi) / Sigsum(exp(yi))
* One-hot Encoding: Needed a way to represent the labels mathematically. The probabilities of correct class is close to 1.0 and all the other classes are close to 0.0, so the vector representation of same thing is called one-hot encoding.
* Cross Entropy: Natural way of comparing two probability vectors is called Cross Entropy. D(S,L) = - sigsum(Li*log(Si)). D = Distance, S = Distributions of softmax, L = Labels which are one-hot encoded.
* Multinomial Logistic Classification D(S(WX+b), L)
* Minimizing Cross Entropy: Calculate the average cross entropy or training loss l = (sigsum,i(D(S(wxi + b), Li)))/N. For example Imagine loss (l) is function w1 and w2 which will be small in some areas and small in othe, our objective is to find the loss minimum for the given weights, we can use "Gradient Descent" and take the derivate - (alpha)(delta(l(w1, w2)))
