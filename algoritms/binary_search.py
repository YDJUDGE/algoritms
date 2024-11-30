
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2

        if item == arr[mid]:
            return mid

        if mid > item:
            high = mid - 1

        else:
            low = mid + 1

    return None

print(binary_search([1, 2, 3, 5, 6, 9, 10, 11, 16], 3))
