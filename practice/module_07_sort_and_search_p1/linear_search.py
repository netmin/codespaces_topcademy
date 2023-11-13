import random


def linear_search(arr: list[int], target: int) -> int:

    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found


def test_linear_search():
    """
    Tests the linear_search function with different scenarios.
    """
    test_arr = [random.randint(0, 100) for _ in range(10)]  # Random array of 10 elements
    target_in_list = test_arr[5]  # A target that is guaranteed to be in the list
    target_not_in_list = 101  # A target that is not in the list

    assert linear_search(test_arr, target_in_list) == test_arr.index(
        target_in_list), "Test case 1 failed (target in list)"
    assert linear_search(test_arr, target_not_in_list) == -1, "Test case 2 failed (target not in list)"
    assert linear_search([], 5) == -1, "Test case 3 failed (empty list)"
    assert linear_search([100], 100) == 0, "Test case 4 failed (single element)"

    print("All test cases passed!")


test_linear_search()
