class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        fast = 1
        slow = 1
        while fast < len(nums):
            if nums[fast-1] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        print(slow)
        return slow

a = Solution()
a.removeDuplicates([1,1,2])