class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[right] == val:
                right -= 1
                continue

            if nums[left] == val:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
            left += 1

        return min(left, right) + 1