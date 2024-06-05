class Solution:
    # 根据当前坐标上能够承载多少单位雨水来思考
    def trap(self, height: [int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        max_left[0] = height[0]
        max_right[-1] = height[-1]

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i])
        for i in range(len(height)-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])

        area = 0
        for i in range(len(height)):
            area += max(min(max_left[i], max_right[i]) - height[i], 0)

        return area