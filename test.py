def window_sum(arr, k):
    temp_sum = sum(arr[:k])
    max_sum = temp_sum
    l = 0
    r = k - 1
    while r < len(arr) and l < r:
        temp = temp_sum - arr[l]
        l += 1
        temp = temp + arr[r]
        max_sum = max(max_sum, temp)
    return max_sum


# arr = [-1, 2, 3, 3, 5, -1]
# k = 4

# print(window_sum(arr, k))


def longest_subarry(arr, k):
    l, r = 0, 0
    long_len = l - r + 1
    while l <= r and r < len(arr):
        temp_sum = sum(arr[l : r + 1])
        if temp_sum <= k:
            long_len = max(long_len, r - l + 1)
            r += 1
        else:
            l += 1

    return long_len


arr = [2, 5, 1, 7, 10]
k = 14
print(longest_subarry(arr, k))
