def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        mid = array[0]
        left = [x for x in array if x <= mid]
        right = [x for x in array if x > mid]
        return quick_sort(left) + [mid] + quick_sort(more_than_pivot)
