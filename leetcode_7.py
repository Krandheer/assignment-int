class Solution:
    """Given a signed 32-bit integer x, return x with its digits reversed. If
    reversing x causes the value to go outside the signed 32-bit integer range
    [-231, 231 - 1], then return 0."""

    def reverse(self, x: int) -> int:
        if x >= 2**31 - 1 or x <= -(2**31):
            return 0
        s = str(x)
        reverse_val = s[::-1]
        if reverse_val[-1] == "-":
            reverse_val = "-" + reverse_val
            reverse_val = reverse_val[: len(reverse_val) - 1]
        reverse_val = int(reverse_val)
        if reverse_val >= 2**31 - 1 or reverse_val <= -(2**31):
            return 0
        return reverse_val


# test
# sol = Solution()
# # x = 123
# x = -123
# res = sol.reverse(x)
# print(res)
