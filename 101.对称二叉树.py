# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        self.res = True
        if not root.left and not root.right:
            return self.res
        elif not (root.left and root.right):
            return False
        else:
            self.recursion(root.left, root.right)
            return self.res

    def recursion(self, l: TreeNode, r: TreeNode):
        if not l and not r:
            return

        if not (l and r):
            self.res = False
            return

        if l.val != r.val:
            self.res = False
            return

        self.recursion(l.left, r.right)
        self.recursion(l.right, r.left)