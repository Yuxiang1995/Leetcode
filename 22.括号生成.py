class Solution:
    '''
    1, -1分别代表'('和')', 用字符串的和来限制不合规的组合，
    并设定终止条件， 递归下去吧！
    '''

    def __init__(self):
        self.limit = 0
        self.res = []

    def generateParenthesis(self, n: int):
        self.limit = n << 1
        if n > 0:
            self.recursion('', 0, 1, n-1, n)
        return self.res

    def recursion(self, tmp, value, next, left, right):
        value += next
        if value < 0:
            return

        if next == 1:
            tmp += '('
        else:
            tmp += ')'

        if len(tmp) == self.limit:
            if next == 1:
                return
            else:
                self.res.append(tmp)
                return

        if left:
            self.recursion(tmp, value, 1, left-1, right)
        if right:
            self.recursion(tmp, value, -1, left, right-1)


class Solution1:
    def generateParenthesis(self, n: int):
        result = {''}
        for i in range(n):    # 共插入n对'()'
            temp = set()
            for s in result:  # 在上一次的结果的所有字符串的各个位置上插入'()'
                for j in range(len(s) + 1):
                    temp.add(s[:j] + '()' + s[j:])  # 利用set的去重机制
            result = temp
        return list(result)


if __name__ == '__main__':
    s = Solution()
    res = s.generateParenthesis(4)
    print(res)