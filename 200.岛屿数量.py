class Node:
    def __init__(self, n):
        self.val = n

class Solution:
    def numIslands(self, grid) -> int:
        init = Node(0)
        flag = [[init for i in range(len(grid[0])+1)] for i in range(len(grid)+1)]
        mmax = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    if flag[i+1][j].val == 0 and flag[i][j+1].val == 0:
                        mmax += 1
                        n = Node(mmax)
                        print(i, j, 'add')
                        flag[i+1][j+1] = n
                    elif (flag[i+1][j].val * flag[i][j+1].val) == 0:
                        flag[i+1][j+1] = flag[i+1][j] if (flag[i+1][j].val > flag[i][j+1].val) else flag[i][j+1]
                    elif flag[i+1][j].val == flag[i][j+1].val:
                        if i == 8 and j == 2:
                            print(flag[i+1][j].val, flag[i][j+1].val)
                        flag[i+1][j+1] = flag[i][j+1]
                    elif flag[i+1][j].val != flag[i][j+1].val:
                        print(i, j, 'delete')
                        mmax -= 1
                        if (flag[i+1][j].val < flag[i][j+1].val):
                            flag[i+1][j+1] = flag[i+1][j]
                            flag[i][j+1].val = flag[i+1][j].val
                        else:
                            flag[i+1][j+1] =flag[i][j+1]
                            flag[i+1][j].val = flag[i+1][j+1].val
        temp = []
        for i in range(len(flag)):
            tmp = []
            for j in range(len(flag[0])):
                tmp.append(flag[i][j].val)
            # temp.append(tmp)
            print(tmp)
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
