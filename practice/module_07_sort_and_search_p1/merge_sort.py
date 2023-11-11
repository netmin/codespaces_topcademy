def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def test_merge_sort():
    # Test random array
    test_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    merge_sort(test_arr)
    assert test_arr == sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), "Failed test for random array"

    # Test empty array
    test_arr = []
    merge_sort(test_arr)
    assert test_arr == [], "Failed test for empty array"

    # Test single element array
    test_arr = [1]
    merge_sort(test_arr)
    assert test_arr == [1], "Failed test for single element array"

    # Test already sorted array
    test_arr = [1, 2, 3, 4, 5]
    merge_sort(test_arr)
    assert test_arr == [1, 2, 3, 4, 5], "Failed test for already sorted array"

    # Test reverse sorted array
    test_arr = [5, 4, 3, 2, 1]
    merge_sort(test_arr)
    assert test_arr == [1, 2, 3, 4, 5], "Failed test for reverse sorted array"

    print("All tests passed!")


test_merge_sort()
