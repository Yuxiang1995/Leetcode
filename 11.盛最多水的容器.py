class Solution:
    def maxArea(self, height: [int]) -> int:
        n = len(height)
        final_maxArea = 0
        left = 0
        right = n - 1
        while left < right:
            curr_Area = min(height[left], height[right]) * (right - left)
            if curr_Area > final_maxArea:
                final_maxArea = curr_Area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return final_maxArea