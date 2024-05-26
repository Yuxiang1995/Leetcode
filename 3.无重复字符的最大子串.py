class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        left, right = 0, 1
        queue_set = set(s[0])
        max_length = 0
        while right < len(s):
            if s[right] not in queue_set:
                queue_set.add(s[right])
                right += 1
            else:
                queue_set.remove(s[left])
                left += 1
            max_length = max(max_length, right - left)
        max_length = max(max_length, len(s) - left)
        return max_length


s = Solution()
p = "pwwkew"
print(s.lengthOfLongestSubstring(p))