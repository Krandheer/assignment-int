import time


def find_triplet(nums, target_sum):
    """brute force approach"""
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target_sum:
                    print(f"{nums[i]} {nums[j]} {nums[k]}")


def find_triplet2(nums, target_sum):
    for i in range(len(nums) - 2):
        arr = dict()  # this will make lookups constant time in average case
        for j in range(i + 1, len(nums)):
            temp = target_sum - nums[i] - nums[j]
            if temp in arr:
                print(f"{nums[i]} {nums[j]} {temp}")
            else:
                arr[nums[j]] = 1


arr = [0, -1, 2, -3, 1]
target = -2

find_triplet2(arr, target)
find_triplet(arr, target)
