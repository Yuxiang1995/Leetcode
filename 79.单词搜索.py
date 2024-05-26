class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        def dfs(word: str, i, j, trace):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False

            if (i, j) in trace:
                return False

            if board[i][j] == word[0]:
                if len(word) == 1:
                    return True
                trace += [(i, j)]
                return dfs(word[1:], i-1, j, trace.copy()) | dfs(word[1:], i+1, j, trace.copy()) | dfs(word[1:], i, j-1, trace.copy()) | dfs(word[1:], i, j+1, trace.copy())
            else:
                return False

        for m in range(len(board)):
            for n in range(len(board[0])):
                trace = []
                flag = dfs(word, m, n, trace)
                # print(flag)
                if flag:
                    return True

        return False

s = Solution()
board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"
s.exist(board, word)