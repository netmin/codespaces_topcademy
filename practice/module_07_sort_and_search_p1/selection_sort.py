def selection_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        # Initially, assume the first element of the unsorted part is the smallest.
        min_index = i
        for j in range(i + 1, n):
            # Update min_index if a smaller element is found.
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part.
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def test_selection_sort():
    """
    Tests the selection_sort function with various inputs.
    """
    assert selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64], "Test case 1 failed"
    assert selection_sort([5, 3, 6, 8, 1, 2]) == [1, 2, 3, 5, 6, 8], "Test case 2 failed"
    assert selection_sort([7, 5, 6, 4]) == [4, 5, 6, 7], "Test case 3 failed"
    assert selection_sort([]) == [], "Test case 4 failed (empty list)"
    assert selection_sort([1]) == [1], "Test case 5 failed (single element)"

    print("All test cases passed!")


test_selection_sort()
