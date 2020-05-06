import numpy as np


def dist(x, y):
    return (x - y)**2


def get_min(m0, m1, m2, i, j):
    if m0 < m1:
        if m0 < m2:
            return i - 1, j, m0
        else:
            return i - 1, j - 1, m2
    else:
        if m1 < m2:
            return i, j - 1, m1
        else:
            return i - 1, j - 1, m2


def spring(data_x, query_y, epsilon):
    Tx = len(data_x)
    Ty = len(query_y)

    C = np.zeros((Tx, Ty))
    B = np.zeros((Tx, Ty, 2), np.int32)
    S = np.zeros((Tx, Ty), np.int32)

    C[0, 0] = dist(data_x[0], query_y[0])

    for j in range(1, Ty):
        C[0, j] = C[0, j - 1] + dist(data_x[0], query_y[j])
        B[0, j] = [0, j - 1]
        S[0, j] = S[0, j - 1]

    for i in range(1, Tx):
        C[i, 0] = dist(data_x[i], query_y[0])
        B[i, 0] = [0, 0]
        S[i, 0] = i

        for j in range(1, Ty):
            pi, pj, m = get_min(C[i - 1, j],
                                C[i, j - 1],
                                C[i - 1, j - 1],
                                i, j)
            C[i, j] = dist(data_x[i], query_y[j]) + m
            B[i, j] = [pi, pj]
            S[i, j] = S[pi, pj]

        imin = np.argmin(C[:(i + 1), -1])
        dmin = C[imin, -1]

        if dmin > epsilon:
            continue

        for j in range(1, Ty):
            if (C[i, j] < dmin) and (S[i, j] < imin) and i != (Tx - 1):
                break
        else:
            path = [[imin, Ty - 1]]
            temp_i = imin
            temp_j = Ty - 1

            while (B[temp_i, temp_j][0] != 0 or B[temp_i, temp_j][1] != 0):
                path.append(B[temp_i, temp_j])
                temp_i, temp_j = path[-1]

            C[S <= imin] = 100000000
            yield np.array(path), dmin


if __name__ == '__main__':
    import pylab as plt
    import pickle

    with open("../test_data.pkl", "rb") as f:
        X, Y = pickle.load(f)

    pathes = []
    plt.plot(X, label="data")
    plt.plot(Y, label="query")
    for path, cost in spring(X, Y, 80):
        plt.plot(path[:, 0], X[path[:, 0]], C="C2", label="matched")
        pathes.append(path)
    plt.legend()
    plt.show()
    print(len(pathes))
