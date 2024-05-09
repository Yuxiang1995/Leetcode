class Solution:
    def solve(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def infect(board, src, dst, i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if board[i][j] == src:
                board[i][j] = dst
                infect(board, src, dst, i-1, j)
                infect(board, src, dst, i+1, j)
                infect(board, src, dst, i, j-1)
                infect(board, src, dst, i, j+1)

        # 保护边界的岛
        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    if board[i][j] == 'O':
                        infect(board, 'O', 'E', i, j)
        
        # 填充并恢复
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'