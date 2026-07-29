class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_val = {}
        for i, val in enumerate(nums):
            pos_val[i] = val
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if pos_val[i] + pos_val[j] == target:
                    return [i,j]
        
