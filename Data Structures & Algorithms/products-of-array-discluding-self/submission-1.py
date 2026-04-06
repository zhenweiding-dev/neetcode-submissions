class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        i lst of int, nums
        o lst, output[i] = product of all expect nums[i]
        c product 32-bit int; o(n) & no division; len(nums) >= 2
        e some elements are 0
        """
        length = len(nums)
        res = [1] * length

        prefix = 1
        
        for i in range(length):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(length - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        

