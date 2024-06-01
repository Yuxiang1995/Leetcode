class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        coins = sorted(coins)
        # print(coins)
        dp = [999999] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i < coin:
                    break
                dp[i] = min(dp[i], dp[i-coin]+1)

        if dp[amount] == 999999:
            return -1
        else:
            return dp[amount]


coins = [1,2,5]
amount = 11
s = Solution()
print(s.coinChange(coins, amount))