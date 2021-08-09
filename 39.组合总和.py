class Solution:
    def combinationSum(self, candidates, target: int):
        self.can = candidates
        self.res = []
        self.minimum = min(candidates)
        self.findTarget(target, [], 0)
        return self.res

    def findTarget(self, target, tmp, index):
        if target == 0:
            self.res.append(tmp)
            return

        if target < self.minimum:
            return

        for i in range(index, len(self.can)):
            tt = tmp.copy()
            tt.append(self.can[i])
            self.findTarget(target-self.can[i], tt, i)


if __name__ == '__main__':
    candidates = [2]
    target = 1
    ss = Solution()
    res = ss.combinationSum(candidates, target)
    print(res)