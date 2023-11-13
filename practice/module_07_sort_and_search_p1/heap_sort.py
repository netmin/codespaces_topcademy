def heapify(arr: list[int], n: int, i: int) -> None:
    """
    Transforms a subtree rooted at index i into a max heap.

    Args:
    arr (list of int): The list of numbers.
    n (int): The size of the heap.
    i (int): The index of the subtree root.
    """
    largest = i  # Assume root is the largest at the beginning
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If left child is larger than root
    if left < n and arr[largest] < arr[left]:
        largest = left

    # If right child is larger than the largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If the largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap elements
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort(arr: list[int]) -> None:
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move current root to the end
        heapify(arr, i, 0)


def test_heap_sort():
    test_data = [12, 11, 13, 5, 6, 7]
    heap_sort(test_data)
    assert test_data == [5, 6, 7, 11, 12, 13], "Test case 1 failed"

    test_data = [1, 12, 9, 5, 6, 10]
    heap_sort(test_data)
    assert test_data == [1, 5, 6, 9, 10, 12], "Test case 2 failed"

    test_data = [10, 7, 8, 9, 1, 5]
    heap_sort(test_data)
    assert test_data == [1, 5, 7, 8, 9, 10], "Test case 3 failed"

    test_data = []
    heap_sort(test_data)
    assert test_data == [], "Test case 4 failed (empty list)"

    test_data = [1]
    heap_sort(test_data)
    assert test_data == [1], "Test case 5 failed (single element)"

    print("All test cases passed!")


test_heap_sort()
