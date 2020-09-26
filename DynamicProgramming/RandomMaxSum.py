# given a list of random numbers, chose a series of numbers from this list, making the sum largest
# every twos numbers that we chose from original list are not adjacent.

import numpy as np


def max_sum(arr, i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    else:
        return max(max_sum(arr, i-2)+arr[i], max_sum(arr, i-1))


def dp_max_sum(arr):
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = arr[1]
    for i in range(2, len(arr)):
        A = opt[i-2]+arr[i]
        B = opt[i-1]
        opt[i] = max(A, B)
    return opt[len(arr)-1]


if __name__ == "__main__":
    arr = [1, 2, 4, 1, 7, 8, 3]
    print(max_sum(arr, 6))
    print(dp_max_sum(arr))

