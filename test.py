def window_sum(arr, k):
    """find the maximum sum of by picking k element consecutively"""
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
    """longest subarray with sum less than or equal to k"""
    l, r = 0, 0
    long_len = l - r + 1
    temp_sum = 0
    while l <= r and r < len(arr):
        temp_sum += arr[r]
        if temp_sum <= k:
            long_len = max(long_len, r - l + 1)
            r += 1
        else:
            temp_sum -= arr[l]
            l += 1

    return long_len


# arr = [2, 5, 1, 7, 10]
# k = 14
# print(longest_subarry(arr, k))


def fruit_into_basket(arr, k):
    """given k basket find maximum number of fruits you can put in
    you have to start from beginning in array and you can't jump
    and you can put only one type of fruit in one basket"""

    # basically if i have k = 2, then I need to find the maximum
    # length of substring having only two type of elements consecutively
    temp = set()
    i, j = 0, 0
    max_len = j - i + 1

    while i <= j and j < len(arr):
        if len(temp) < k:
            if arr[j] not in temp:
                temp.add(arr[j])
                max_len = max(max_len, j - i + 1)
                j += 1
            else:
                max_len = max(max_len, j - i + 1)
                j += 1
        elif len(temp) == k:
            if arr[j] in temp:
                max_len = max(max_len, j - i + 1)
                j += 1
            else:
                temp = set()
                i = j - 1
                temp.add(arr[i])
                if arr[j] not in temp:
                    temp.add(arr[j])
    return max_len


# arr = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
# print(fruit_into_basket(arr, 2))


def nth_root(n, m):
    # given two number find a nth room of m such that x**n = m
    """we know the root will be less than m, basically between 1, m"""
    low = 1
    high = m - 1
    while low <= high:
        mid = (low + high) // 2
        if mid**n == m:
            return mid
        if mid**n >= m:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(nth_root(3, 64))
