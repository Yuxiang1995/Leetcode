# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.res = 0
        self.recursion(root, 0)
        return self.res

    def recursion(self, node:TreeNode, depth):
        if node:
            depth += 1
        else:
            self.res = max(self.res, depth)
            return

        self.recursion(node.left, depth)
        self.recursion(node.right, depth)