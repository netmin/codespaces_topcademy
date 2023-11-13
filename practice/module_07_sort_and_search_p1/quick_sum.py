def quick_sum(arr: list[int]) -> int:
    if not arr:
        return 0
    else:
        return arr[0] + quick_sum(arr[1:])
