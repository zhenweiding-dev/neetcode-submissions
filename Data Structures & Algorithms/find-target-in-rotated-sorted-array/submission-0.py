class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        i a sorted array, but rotated, target
        o index of target if exist else -1
        c elements are unique; o(log n)
        e 
        if we split the array into 2, 1 must be sorted one
        if we can find target in a sorted one, it's simple binary search
        
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
        
            if nums[l] <= nums[mid]: #left part is sorted
                if target > nums[mid] or target < nums[l]:
                    #not in this part
                    l = mid + 1
                else:
                    #in this part
                    r = mid - 1
            else:
                if target > nums[r] or target < nums[mid]:
                #not in this part
                    r = mid - 1
                else: # in this part
                    l = mid + 1
        return -1
    

