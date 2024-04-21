class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> [float]:
        level_nodes = [root]
        result = []
        while level_nodes:
            nums = len(level_nodes)
            sum = 0
            tmp_nodes = []
            for node in level_nodes:
                sum += node.val
                if node.left:
                    tmp_nodes.append((node.left))
                if node.right:
                    tmp_nodes.append((node.right))
            result.append(sum / nums)
            level_nodes = tmp_nodes
        return result