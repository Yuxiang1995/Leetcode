class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        for i, num in enumerate(nums):
            index = (num - 1) % n
            nums[index] += n
        print(nums)

        res = []
        for i, num in enumerate(nums):
            if num <= n:
                res.append(i + 1)
        return res

if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    s = Solution()
    print(s.findDisappearedNumbers(nums))