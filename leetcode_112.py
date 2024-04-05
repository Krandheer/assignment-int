def hasPathSum(root: TreeNode, sum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right and (sum - root.val) == 0:
        return True
    return hasPathSum(root.left, sum - root.val) or hasPathSum(
        root.right, sum - root.val
    )
