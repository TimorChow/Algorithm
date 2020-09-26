# coding:utf-8

# 给定一个数组 {3, 1, 2, 1} 和一个数字k =4。求这个数组的一个最长连续子数组，
# 这个最长连续子数组中所有数字的和必须小于或等于k。


def longest_sub_array(array, k):
    result = []
    longest_sub = []

    # 找出所有子数组, 并过滤
    for num in range(1, len(array)+1):
        # 1. 倒数第num-1个元素不需要当做开始来数, 因为肯定不能满足num个
        # for i in range(0, len(array)-num+1):
        #     print(num, i, array[i: i+num])


        # 2. 当第i个元素+预计数组长度大于原数组长度时, 无法找到这样的数组, 所以pass
        for i in range(0, len(array)):
            if i+num > len(array):
                continue
            arr = array[i: i+num]
            # this subarray match two conditions in the meanwhile
            # 1. if the sum is smaller than or equals k
            # 2. if it is the longest subarray
            if sum(arr) <= k and len(arr) > len(longest_sub):
                longest_sub = arr
    return longest_sub


if __name__ == "__main__":
    array = [3, 1, 2, 2, 2, 1, 1]
    k = 5
    print(longest_sub_array(array, k))
