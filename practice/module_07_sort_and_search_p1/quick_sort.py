def quick_sort(arr: list[int]) -> list[int]:

    if len(arr) <= 1:
        return arr  # A list with 0 or 1 element is already sorted

    pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort and combine


# Simple tests for quick sort
def test_quick_sort():
    assert quick_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10], "Test case 1 failed"
    assert quick_sort([5, 3, 7, 10, 4, 1, 4]) == [1, 3, 4, 4, 5, 7, 10], "Test case 2 failed"
    assert quick_sort([25, 22, 21, 10, 3, 2, 1]) == [1, 2, 3, 10, 21, 22, 25], "Test case 3 failed"
    assert quick_sort([]) == [], "Test case 4 failed (empty list)"
    assert quick_sort([1]) == [1], "Test case 5 failed (single element)"

    print("All test cases passed!")


test_quick_sort()
