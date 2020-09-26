# coding:utf-8 -*-


# 暴力法
# def max_sub_array(array):
#     max_sum = array[0]
#     length = len(array)
#     for i in range(0, length):
#         for j in range(i, length):
#             curry_sum = 0
#             for k in range(i, j):
#                 curry_sum += array[k]
#             if curry_sum > max_sum:
#                 print i, k
#                 max_sum = curry_sum
#     return max_sum


# 分治，二分法
#
def max_sub_array(array):
    if len(array) == 1:
        return array[0]
    middle = len(array)//2
    sum_left = max_sub_array(array[0:middle])
    sum_right = max_sub_array(array[middle+1:len(array)])

    left_max_sum = array[middle]
    curry_sum = array[middle]
    for i in range(middle, -1, -1):
        curry_sum += array[i]
        if curry_sum >= left_max_sum:
            left_max_sum = curry_sum

    right_max_sum = array[middle+1]
    curry_sum = array[middle+1]
    for j in range(middle+1, len(array)):
        curry_sum += array[j]
        if curry_sum >= right_max_sum:
            right_max_sum = curry_sum

    sum_middle = sum_left + sum_right

    max_sum = max([sum_right, sum_left, sum_middle])
    return max_sum

if __name__ == "__main__":
    array_1 = [1, 2, 3, -1, -3, -4, 2, 6, -1]
    print(max_sub_array(array_1))
    # for i in range(len(array_1)-1, -1, -1):
    #     print array_1[i]
