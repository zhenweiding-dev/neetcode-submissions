class Solution:
    def trap(self, height: List[int]) -> int:
        """
        i heigth: lst of int in [0, ]
        o max area
        c len in [1,1000]; h [0, 1000]
        e
        """
        if len(height) < 3:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                if leftMax > height[l]:
                    res += leftMax - height[l]
                else:
                    leftMax = height[l]
            else:
                r -= 1
                if rightMax > height[r]:
                    res += rightMax - height[r]
                else:
                    rightMax = height[r]
        return res
        