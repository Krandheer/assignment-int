from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    ans = []
    arr_len = len(nums)

    # def helper(temp_ans, index):
    #     if index == arr_len:
    #         ans.append(list(temp_ans))
    #         return

    #     temp_ans.append(nums[index])
    #     helper(temp_ans, index + 1)

    #     temp_ans.pop()
    #     helper(temp_ans, index + 1)

    # helper([], 0)

    # another way of doing same
    def helper(temp_ans, arr, index):
        if index == arr_len:
            ans.append(temp_ans[:])
            return

        # take case
        temp_ans.append(arr[0])
        helper(temp_ans, arr[1:], index + 1)

        # not take case
        temp_ans.pop()  # backtracking step
        helper(temp_ans, arr[1:], index + 1)

    helper([], nums, 0)
    # return ans
    # now if problem is about subset
    temp_ans = []
    for i in ans:
        temp_ans.append(sum(i))
    temp_ans.sort()
    return temp_ans


# tests
nums1 = [1, 2, 3]
print(subsets(nums1))
