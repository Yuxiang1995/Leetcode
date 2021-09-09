class Solution:
    def majorityElement(self, nums) -> int:
        # Boyer-Moore 投票算法
        res = 0
        count = 0

        for num in nums:
            if count == 0:
                res = num

            if num == res:
                count += 1
            else:
                count -= 1

        return res


if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    s = Solution()
    print(s.majorityElement(nums))