def sort_halves(arr: list[int]) -> list[int]:
    mid = len(arr) // 2
    # If the length of the list is odd, add one to the middle index for the first half
    if len(arr) % 2 == 1:
        mid += 1
    first_half = sorted(arr[:mid], reverse=True)
    second_half = sorted(arr[mid:])

    return first_half + second_half


def test_sort_halves():
    # Test with an empty list
    assert sort_halves([]) == [], "Empty list should return an empty list"

    # Test with a single element list
    assert sort_halves([1]) == [1], "Single element list should return the same list"

    # Test with an even number of elements
    assert sort_halves([4, 2, 3, 1]) == [4, 2, 1, 3], "Even element list should be sorted correctly"

    # Test with an odd number of elements
    assert sort_halves([5, 3, 1, 4, 2]) == [5, 3, 1, 2, 4], "Odd element list should be sorted correctly"

    # Test with a list already sorted as per the condition
    assert sort_halves([4, 2, 1, 3, 5]) == [4, 2, 1, 3, 5], "Already sorted list should remain unchanged"

    # Test with negative numbers
    assert sort_halves([-3, -1, -2, -4]) == [-1, -3, -4, -2], "List with negative numbers should be sorted correctly"
    # Test with duplicate numbers
    assert sort_halves([2, 2, 3, 3]) == [2, 2, 3, 3], "List with duplicates should be sorted correctly"

    print("All tests passed successfully!")


test_sort_halves()

