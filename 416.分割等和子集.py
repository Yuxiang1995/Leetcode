class Solution:
    def canPartition(self, nums: [int]) -> bool:
        if len(nums) < 2:
            return False
        all_sum = sum(nums)
        if all_sum % 2 == 1:
            return False
        if max(nums) > all_sum / 2:
            return False

        target = int(all_sum / 2)
        dp = [[False for j in range(target + 1)] for i in range(len(nums))]

        # init
        for i in range(len(nums)):
            dp[i][0] = True
        dp[0][nums[0]] = True

        # 遍历
        for i in range(1, len(nums)):
            for j in range(1, target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]


nums = [14,9,8,4,3,2]
s = Solution()
print(s.canPartition(nums))