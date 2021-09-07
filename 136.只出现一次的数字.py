class Solution:
    def singleNumber(self, nums) -> int:
        # 异或运算 牛逼大了
        if len(nums) < 2:
            return nums[0]

        for i in range(1, len(nums)):
            nums[i] ^= nums[i - 1]

        return nums[-1]


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    s = Solution()
    print(s.singleNumber(nums))