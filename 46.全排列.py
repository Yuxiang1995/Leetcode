class Solution:
    def permute(self, nums):
        self.nums = nums
        self.res = []
        self.recursion([])
        return self.res

    def recursion(self, arrange):
        if len(arrange) == len(self.nums):
            self.res.append(arrange)

        for num in self.nums:
            if num not in set(arrange):
                tmp = arrange.copy()
                tmp.append(num)
                self.recursion(tmp)

if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    print(s.permute(nums))