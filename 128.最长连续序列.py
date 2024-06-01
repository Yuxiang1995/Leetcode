class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        if len(nums) < 2:
            return len(nums)

        cache_set = set()
        for num in nums:
            cache_set.add(num)

        max_length = 0
        for num in nums:
            if num - 1 in cache_set:
                continue
            cur_length = 1
            tmp = num + 1
            while tmp in cache_set:
                cur_length += 1
                tmp += 1
            max_length = max(max_length, cur_length)

        return max_length