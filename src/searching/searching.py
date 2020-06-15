def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # return the index if found

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # var setup (lo, hi, mid)
    lo = 0
    hi = len(arr) -1
    mid = 0
    while lo <= hi:
        mid = (hi + lo) // 2  ## need double // to ensure integer
        if arr[mid] == target:
            return mid
        elif target > arr[mid]: # take out lower(left side), set mid to lo
            lo = mid + 1
        else: # take out upper(right side), set mid to hi
            hi = mid -1
    return -1  # not found
