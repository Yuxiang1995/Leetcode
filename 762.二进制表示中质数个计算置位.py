class Solution:
    def __init__(self):
        self.primeSet = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        for num in range(left, right + 1):
            count = 0
            while num:
                if (num - ((num >> 1) << 1)):
                    count += 1
                num = num >> 1
            if count in self.primeSet:
                res += 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimeSetBits(289051, 294301))