def binary_search(arr, left, right, target):
    # left = 0
    # right = len(arr) - 1
    # mid = left + right //

    mid = (left + right) // 2

    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return binary_search(arr, mid + 1, right, target)
    else:
        return binary_search(arr, left, right - 1, target)
