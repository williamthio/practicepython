def binary_search(arr, value):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if value < arr[mid]:
            right = mid - 1
        elif value > arr[mid]:
            left = mid + 1
        else:
            return True
    return False

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(arr, 7))
