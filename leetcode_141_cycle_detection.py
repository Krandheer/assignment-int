class Solution:
    """copy pasted from leetcode 112 problem that I solved there"""

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and (sum - root.val) == 0:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(
            root.right, sum - root.val
        )
