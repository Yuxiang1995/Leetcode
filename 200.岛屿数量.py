class Solution:
    def numIslands(self, grid) -> int:
        def infect(grid, src, dst, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            
            if grid[i][j] == src:
                grid[i][j] = dst
                infect(grid, src, dst, i-1, j)
                infect(grid, src, dst, i+1, j)
                infect(grid, src, dst, i, j-1)
                infect(grid, src, dst, i, j+1)

        nums_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    nums_island += 1
                    infect(grid, '1', '2', i, j)

        return nums_island
        



# if __name__ == '__main__':
#     grid = [["1","1","1","1","1","0","1","1","1","1"],
#             ["1","0","1","0","1","1","1","1","1","1"],
#             ["0","1","1","1","0","1","1","1","1","1"],
#             ["1","1","0","1","1","0","0","0","0","1"],
#             ["1","0","1","0","1","0","0","1","0","1"],
#             ["1","0","0","1","1","1","0","1","0","0"],
#             ["0","0","1","0","0","1","1","1","1","0"],
#             ["1","0","1","1","1","0","0","1","1","1"],
#             ["1","1","1","1","1","1","1","1","0","1"],
#             ["1","0","1","1","1","1","1","1","1","0"]]
#     s = Solution()
#     print(s.numIslands(grid))
