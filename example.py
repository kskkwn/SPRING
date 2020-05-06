import pylab as plt
import pickle
from spring import spring


def main():
    with open("./test_data.pkl", "rb") as f:
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


if __name__ == '__main__':
    main()
