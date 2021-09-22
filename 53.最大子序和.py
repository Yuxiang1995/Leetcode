class Solution:
    def maxSubArray(self, nums) -> int:
        preMax = 0
        maxSum = nums[0]

        for num in nums:
            preMax = max(preMax + num, num)
            maxSum = max(preMax, maxSum)

        return maxSum

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    print(s.maxSubArray(nums))