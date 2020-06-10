def maximum(arr):
    candidate = arr[0]
    for num in arr:
        if candidate < num:
            candidate = num
    return candidate

if __name__ == "__main__":
    print(maximum([3, 4, 5, 2, 1]))
