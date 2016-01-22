import numpy as np
# +1 5:1 8:1 18:1 22:1 36:1 40:1 51:1 61:1 67:1 72:1 75:1 76:1 80:1 83:1

log = np.log

def parse_line(line):
    return 0

def preparse(data):
    w = []
    y = []
    for i, vector in enumerate(data):
        w.append([])
        for j in range(123):
            w[i].append(0) # initialize vector
        vector = vector.split()
        y.append(int(vector.pop(0)))
        for feature in vector:
            t = feature.split(':')
            w[i][int(t[0])] = 1
    print y

def load_file(fname):
    data = []
    with open(fname,'rb') as f:
        data = f.readlines()
    return data

def main():
    f = load_file("a7a.dev")
    preparse(f)

if __name__ == "__main__":
    main()
