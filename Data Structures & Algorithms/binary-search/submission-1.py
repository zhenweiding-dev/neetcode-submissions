class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        i nums:[int], sorted->; target:int
        o index of target or -1
        c O(logn); len(nums) in [1,10000]; nums are unique
        e
        """
        l, r = 0, len(nums) - 1
     
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

        