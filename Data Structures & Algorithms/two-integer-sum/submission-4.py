class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_pos = {}
        for i, val in enumerate(nums):
            val_pos[val] = i
        for i, val in enumerate(nums):
            diff = target - val
            if diff in val_pos and val_pos[diff] != i:
                return [i, val_pos[diff]]
        
        
