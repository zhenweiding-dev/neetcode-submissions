class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        i nums: [int]; k: int
        o lst[max ele in every window]
        c len(nums) in [1,100000], nums[i] in [-10000, 10000], k in [1, len(nums)]
        e len(nums) == 1: [nums[0]]; k == 1: nums
        a fixed window, use temp to store max in current window
        """
        if len(nums) == 1:
            return [nums[0]]
        if k == 1:
            return nums
        
        temp = max(nums[:k])
        res = [temp]
        l = 1
        r = k

        while r < len(nums):
            if nums[r] < nums[l - 1]:
                temp = max(nums[l : r + 1])
    
            elif nums[r] >= nums[l - 1]:
                temp = max(temp, nums[r])
            res.append(temp)
            r += 1
            l += 1
        return res


