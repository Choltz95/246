import numpy as np
import sys
# +1 5:1 8:1 18:1 22:1 36:1 40:1 51:1 61:1 67:1 72:1 75:1 76:1 80:1 83:1

def load_file(fname):
    data = []
    with open(fname,'rb') as f:
        data = f.readlines()
    return data

def preparse(data):
    X = []
    y = []
    for i, vector in enumerate(data):
        X.append([])
        for j in range(124):
            X[i].append(0) # initialize data matrix to zeroes
        vector = vector.split()
        y.append(int(vector.pop(0))) # pop our target vector
        for feature in vector:
            t = feature.split(':')
            X[i][int(t[0])] = 1

    X_mat = np.matrix(X, dtype=int) # convert our data array to matrix
    y_mat = np.array(y,dtype = int) # convert our target to vector
    return X_mat, y_mat

def compute_model(X, y, l = 78): # acceptable lambda found through manual experimentation with .dev set
    n_col = X.shape[1]
    f = np.linalg.lstsq(X.T.dot(X) + l * np.identity(n_col), np.squeeze(np.asarray(X.T.dot(y)))) # Regularized linear regression w/ normal equation
    return f

def main():
    f1 = load_file("a7a.train")
    X, y= preparse(f1)
    W = compute_model(X,y)

    f2 = load_file(sys.argv[1])
    X2, y2 = preparse(f2)
    result = np.squeeze(np.asarray(X2)).dot(W[0]) # compute our resultt

    correct = 0.0
    for i, r in enumerate(result): # calculate accuracy
        if r > 0 and y2[i] == 1:
            correct = correct + 1.0
        if r < 0 and y2[i] == -1:
            correct = correct + 1.0

    print(str(correct) + " correct predictions for " + str(y2.shape[0]) + " points")   
    print("The accuracy is " + str(correct/y2.shape[0]))   

if __name__ == "__main__":
    main()