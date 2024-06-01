class Solution:
    # 主要就是判断偷不偷第n间，进行讨论
    def rob(self, nums: [int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[-1]