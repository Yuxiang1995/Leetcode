# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 利用二叉搜索树的性质，中序遍历的结果就是升序数组  
class Solution:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        sorted_list = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            sorted_list.append(root.val)
            root = root.right
        # print(sorted_list)
        return sorted_list[k-1]