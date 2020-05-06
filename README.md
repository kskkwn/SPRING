# SPRING
This is an unofficial python implementation of the SPRING algorithm, which is a partial matching for time series with Dynamic Time Warping


# Install
```bash
pip3 install git+https://github.com/kskkwn/SPRING.git
```

# Example
```python
    import pylab as plt
    import pickle
    from spring import spring

    with open("../test_data.pkl", "rb") as f:
        X, Y = pickle.load(f)

    pathes = []
    plt.plot(X, label="data")
    plt.plot(Y, label="query")
    for path, cost in spring(X, Y, thresold=80):
        plt.plot(path[:, 0], X[path[:, 0]], C="C2", label="matched")
        pathes.append(path)
    plt.legend()
    plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/3478423/81132490-8b627b00-8f89-11ea-9285-e8c597067512.png)





# Reference
Yasushi Sakurai, Christos Faloutsos, and Masashi Yamamuro. "Stream monitoring under the time warping distance." 2007 IEEE 23rd International Conference on Data Engineering. IEEE, 2007.

