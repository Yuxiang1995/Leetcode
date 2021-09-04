class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[-1][-1] = grid[-1][-1]

        for i in range(m - 2, -1, -1):
            dp[i][-1] = dp[i + 1][-1] + grid[i][-1]
        for j in range(n - 2, -1, -1):
            dp[-1][j] = dp[-1][j + 1] + grid[-1][j]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]

        return dp[0][0]


if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    s = Solution()
    print(s.minPathSum(grid))