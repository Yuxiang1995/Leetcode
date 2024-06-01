class Solution:
    # dp[i] = min(dp[i-cj]) + 1
    def numSquares(self, n: int) -> int:
        candidate_list = []

        x = 1
        while pow(x, 2) <= n:
            candidate_list.append(pow(x, 2))
            x += 1

        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            min_count = 99999
            for square in candidate_list:
                if square > i:
                    break
                min_count = min(min_count, dp[i - square])
            dp[i] = min_count + 1

        return dp[-1]