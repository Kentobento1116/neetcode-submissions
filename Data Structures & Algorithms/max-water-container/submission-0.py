class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        p1 = 0
        p2 = len(heights) - 1

        while p1 < p2:
            if (p2 - p1) * min(heights[p1], heights[p2]) > max_area:
                max_area = (p2 - p1) * min(heights[p1], heights[p2])
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        
        return max_area
