class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxLength = 0
        self.dfs(root)
        return self.maxLength

    def dfs(self, root: TreeNode):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.maxLength = max(self.maxLength, left + right)
        return max(left, right) + 1