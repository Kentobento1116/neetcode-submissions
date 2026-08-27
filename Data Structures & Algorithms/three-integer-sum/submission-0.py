class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        res = []

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if s[i] + s[l] + s[r] == 0:
                    res.append([s[i], s[l], s[r]])
                
                if s[i] + s[l] + s[r] > 0:
                    r -= 1
                else:
                    l += 1
        
        return [list(t) for t in set(tuple(l) for l in res)]

