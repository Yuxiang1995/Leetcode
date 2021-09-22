class Solution:
    def maxSubArray(self, nums) -> int:
        preMax = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            if preMax > 0:
                preMax += nums[i]
            else:
                preMax = nums[i]
            maxSum = max(maxSum, preMax)

        return maxSum

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    print(s.maxSubArray(nums))