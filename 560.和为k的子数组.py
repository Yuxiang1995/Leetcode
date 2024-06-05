class Solution:
    # 前缀和 + 哈希
    def subarraySum(self, nums: [int], k: int) -> int:
        pre_sum = [0] * len(nums)
        tmp_sum = 0
        for i, num in enumerate(nums):
            tmp_sum += num
            pre_sum[i] = tmp_sum

        count_dict = {0: 1}
        res = 0
        for p_sum in pre_sum:
            target = p_sum - k
            if target in count_dict:
                res += count_dict[target]

            if p_sum in count_dict:
                count_dict[p_sum] += 1
            else:
                count_dict[p_sum] = 1
        
        return res