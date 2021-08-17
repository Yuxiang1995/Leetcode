class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        for i in range(32):
            if (x % 2) != (y % 2):
                count += 1
            x = x >> 1
            y = y >> 1

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 3))