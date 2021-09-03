class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        mat = [[1 for i in range(n)] for j in range(m)]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                mat[i][j] = mat[i+1][j] + mat[i][j+1]

        return mat[0][0]



if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 10))