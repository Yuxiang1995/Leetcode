class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_length = max(len(a), len(b))
        a = a.zfill(max_length)
        b = b.zfill(max_length)

        pt = max_length - 1
        add = 0
        new_str = ""
        while pt >= 0:
            sum = int(a[pt]) + int(b[pt]) + add
            if sum > 1:
                add = 1
            else:
                add = 0
            sum = sum % 2
            new_str += str(sum)
            pt -= 1
        if add:
            new_str += '1'

        return new_str[::-1]