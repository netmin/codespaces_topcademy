def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def test_binary_search():
    """
    Test cases for the binary_sort function.
    """
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 4, "Test case 1 failed"
    assert binary_search([10, 22, 31, 45, 53, 60, 70, 85, 92, 100], 85) == 7, "Test case 2 failed"
    assert binary_search([10, 22, 31, 45, 53, 60, 70, 85, 92, 100], 10) == 0, "Test case 3 failed"
    assert binary_search([10, 22, 31, 45, 53, 60, 70, 85, 92, 100], 100) == 9, "Test case 4 failed"
    assert binary_search([10, 22, 31, 45, 53, 60, 70, 85, 92, 100], 11) == -1, "Test case 5 failed"
    assert binary_search([], 5) == -1, "Test case 6 failed (empty list)"
    assert binary_search([5], 5) == 0, "Test case 7 failed (single element)"

    print("All test cases passed!")


test_binary_search()
