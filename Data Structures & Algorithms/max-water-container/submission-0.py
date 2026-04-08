class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        i lst of int
        o max((index2 -index1)*min))
        c height[i] in [0,1000]; len in [2, 1000]
        e 
        """
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            water = (r - l) * min(heights[l], heights[r])
            res = max(res, water)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
