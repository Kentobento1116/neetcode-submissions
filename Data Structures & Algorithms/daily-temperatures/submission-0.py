class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (index, temp)
        res = [0] * len(temperatures)
        for curr_i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                lower_index, lower_temp = stack.pop()
                res[lower_index] = curr_i - lower_index
            stack.append((curr_i, temp))
        return res    
                    
