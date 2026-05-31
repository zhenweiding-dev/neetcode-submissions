class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        i len(nums) = n, nums sorted in asending but rotated
        o min(nums)
        c o(log n)
        e
        rotated means the array has two sorted parts
        compare the begin and end find smaller parts
        if begin is smaller, its the begin
        else min is between the begin and end
        loop find the element smaller than it's right
        from mid, if bigger than l, then l = mid + 1; elif smaller than l, r = mid
        keep loop until l = r
        """
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[r]