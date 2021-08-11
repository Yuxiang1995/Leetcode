class Node:
    def __init__(self, n):
        self.val = n

class Solution:
    def numIslands(self, grid) -> int:

        def infect(i, j, src, dst, flag):
            if i < 1 or j < 1 or i >=len(flag) or j >= len(flag[0]):
                return

            if flag[i][j] == src:
                flag[i][j] = dst
                infect(i - 1, j, src, dst, flag)
                infect(i, j - 1, src, dst, flag)
                infect(i, j + 1, src, dst, flag)
                infect(i + 1, j, src, dst, flag)
            else:
                return

        init = Node(0)
        flag = [[init for i in range(len(grid[0])+1)] for i in range(len(grid)+1)]
        node_list = []
        mmax = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    if flag[i+1][j].val == 0 and flag[i][j+1].val == 0:
                        mmax += 1
                        n = Node(mmax)
                        node_list.append(n)
                        flag[i+1][j+1] = n
                    elif (flag[i+1][j].val * flag[i][j+1].val) == 0:
                        flag[i+1][j+1] = flag[i+1][j] if (flag[i+1][j].val > flag[i][j+1].val) else flag[i][j+1]

                    elif flag[i+1][j].val == flag[i][j+1].val:
                        flag[i+1][j+1] = flag[i][j+1]
                    elif flag[i+1][j].val != flag[i][j+1].val:
                        mmax -= 1
                        for node in node_list:
                            if node.val > max(flag[i+1][j].val, flag[i][j+1].val):
                                node.val -= 1
                        if (flag[i+1][j].val < flag[i][j+1].val):
                            flag[i+1][j+1] = flag[i+1][j]
                            infect(i, j + 1, flag[i][j+1], flag[i+1][j+1], flag)
                        else:
                            flag[i+1][j+1] = flag[i][j+1]
                            infect(i + 1, j, flag[i+1][j], flag[i+1][j+1], flag)

        return mmax



if __name__ == '__main__':
    grid = [["1","1","1","1","1","0","1","1","1","1"],
            ["1","0","1","0","1","1","1","1","1","1"],
            ["0","1","1","1","0","1","1","1","1","1"],
            ["1","1","0","1","1","0","0","0","0","1"],
            ["1","0","1","0","1","0","0","1","0","1"],
            ["1","0","0","1","1","1","0","1","0","0"],
            ["0","0","1","0","0","1","1","1","1","0"],
            ["1","0","1","1","1","0","0","1","1","1"],
            ["1","1","1","1","1","1","1","1","0","1"],
            ["1","0","1","1","1","1","1","1","1","0"]]
    s = Solution()
    print(s.numIslands(grid))
