# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        self.res = []
        self.recursion([root])
        return self.res

    def recursion(self, treeList):
        if not treeList:
            self.res = self.res[:-1]
            return
        tmp = []
        nextList = []
        for node in treeList:
            if not node:
                continue
            tmp.append(node.val)
            nextList.append(node.left)
            nextList.append(node.right)
        self.res.append(tmp)
        self.recursion(nextList)