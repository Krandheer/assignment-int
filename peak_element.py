def peak_element(nums):
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        if nums[0] >= nums[1]:
            return 0
        return 1

    first = nums[0]
    last = nums[-1]
    peak = 0
    if first >= nums[1]:
        peak = 0
    if last >= nums[-2] and last >= peak:
        peak = len(nums) - 1

    for i in range(1, len(nums) - 1):
        if nums[i - 1] <= nums[i] >= nums[i + 1] and nums[i] >= nums[peak]:
            peak = i
    return peak


# test's

# arr = [1, 2, 3, 1]
# arr = [10, 20, 15, 2, 23, 90, 67]
# print(peak_element(arr))
