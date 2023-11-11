def insertion_sort(numbers: list[int]) -> list[int]:
    # Iterate over each index in the list starting from the second one
    for i in range(1, len(numbers)):
        # The current number to be inserted into the sorted portion of the list
        current = numbers[i]
        # Find the position where this number should be inserted
        j = i - 1
        while j >= 0 and numbers[j] > current:
            numbers[j + 1] = numbers[j]  # Shift the larger number to the right
            j -= 1
        # Insert the current number into the correct position
        numbers[j + 1] = current
        
    return numbers


# Test cases for the insertion_sort function
def test_insertion_sort():
    assert insertion_sort([4, 2, 6, 1, 3, 5]) == [1, 2, 3, 4, 5, 6], "Test with random list of numbers failed"
    assert insertion_sort([]) == [], "Test with empty list failed"
    assert insertion_sort([1]) == [1], "Test with single element list failed"
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test with already sorted list failed"
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Test with reverse sorted list failed"
    assert insertion_sort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3], "Test with all identical elements failed"
    print("All tests passed.")


test_insertion_sort()
