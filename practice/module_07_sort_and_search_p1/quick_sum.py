def quick_sum(arr):
    if not arr:
        return 0
    else:
        return arr[0] + quick_sum(arr[1:])
