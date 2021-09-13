class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.exchange(root)
        return root

    def exchange(self, root:TreeNode):
        if not root:
            return

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.exchange(root.left)
        self.exchange(root.right)