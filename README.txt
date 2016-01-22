Name: Chester Holtz
Email: choltz2@u.rochester.edu
Course: CSC246
Homework: Implement linear regression for the adult income dataset using Python.

************ Files *********
README.txt This file
regression.py My implementation of a linear regression based classifier.
a7a.train data file required to train the weights for our classifier.

************ Algorithm *****
For this project we implement simple linear regression with normal regularization. We construct a matrix X and vector y from the dataset and assume X^TX is invertible to compute the pseudo inverse of X. Our regularization coeficient lambda serves to restrict the magnitude of some parameters that do not assist in prediction, although I did not really choose it carefully.

************ Instructions ***
python regression.py {your test file}

************ Results *******
Results on the dev and test set where good - mid to high 80% accuracy with little to no interaction with the regularization constant lambda.

************ Your interpretation *******
I was not expecting such good accuracy with such a simple classification scheme. With more time I would have liked to further experiment with various lambdas, and perhaps implement a 
scheme to derive the optimal regularization coefficient given a dev set.

************ References ************
texbook