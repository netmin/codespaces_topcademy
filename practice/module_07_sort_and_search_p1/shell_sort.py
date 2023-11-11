def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Initialize the gap size

    # Continuously reduce the gap until it becomes 0
    while gap > 0:
        # Perform a gapped insertion sort
        for i in range(gap, n):
            temp = arr[i]  # Store the current element
            j = i
            # Shift earlier gap-sorted elements up until the correct location is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            # Place temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2  # Reduce the gap for the next iteration

    return arr


def test_shell_sort():
    """
    Test the shellSort function with simple test cases.
    """
    assert shell_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90], "Test case 1 failed"
    assert shell_sort([4, 3, 2, 10, 12, 1, 5]) == [1, 2, 3, 4, 5, 10, 12], "Test case 2 failed"
    assert shell_sort([12, 34, 54, 2, 3]) == [2, 3, 12, 34, 54], "Test case 3 failed"
    assert shell_sort([]) == [], "Test case 4 failed (empty list)"
    assert shell_sort([1]) == [1], "Test case 5 failed (single element)"

    print("All test cases passed!")


test_shell_sort()
