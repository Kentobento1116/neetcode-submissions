class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        pre = 1
        for num in nums:
            prefix.append(pre)
            pre *= num

        suffix = []
        suf = 1
        for num in reversed(nums):
            suffix.append(suf)
            suf *= num

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[len(nums) - i - 1])
        return res
