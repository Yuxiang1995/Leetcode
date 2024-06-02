class Solution:
    # 因为存在负数，所以要维护最大和最小两个dp数组
    def maxProduct(self, nums: [int]) -> int:
        min_dp = [0] * len(nums)
        max_dp = [0] * len(nums)
        min_dp[0], max_dp[0] = nums[0], nums[0]

        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i], nums[i])
            min_dp[i] = min(max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i], nums[i])

        return max(max_dp)