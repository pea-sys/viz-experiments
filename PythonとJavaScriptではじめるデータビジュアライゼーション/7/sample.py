import numpy as np

# 入門
a = np.arange(1, 4)
print(a + a)


def print_array_details(a):
    print("Dimensions: %d, shape: %s, dtype: %s" % (a.ndim, a.shape, a.dtype))


a = np.arange(1, 9)
print(a)
print_array_details(a)

a = a.reshape([2, 4])
print(a)
print_array_details(a)

a = a.reshape([2, 2, 2])
print(a)
print_array_details(a)

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print(x.shape)
x.shape = (6,)
print(x)
x = x.astype("int64")
print(x.dtype)

a = np.zeros([2, 3])
print(a)

print(a.dtype)

print(np.ones([2, 3]))

empty = np.array((2, 3))
print(empty)

print(np.random.random((2, 3)))

print(np.linspace(2, 10, 5))

# 配列

a = np.arange(0, 8)
print(a[2])
print(a[3:5])
print(a[::-1])

print(a < 5)

a = a.reshape((2, 4))
print(a.min(axis=1))
print(a.sum())
print(a.mean())
print(a.std(axis=1))

pi = np.pi
a = np.array([pi, pi / 2, pi / 4, pi / 6])
print(np.degrees(a))

sin_a = np.sin(a)
print(sin_a)

print(np.round(sin_a, 7))
a = np.arange(8).reshape((2, 4))
print(np.cumsum(a, axis=1))
print(np.cumsum(a))


def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1 :] / n


a = np.arange(10)
print(moving_average(a, 4))
