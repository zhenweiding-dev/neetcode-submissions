class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        i lst of nums
        o n: the length of longest consecutive seq
        c len in [0,1000]
        e length 0, 1
        use a set to store nums, so we can find every start of each 
        sequence(num-1 not in the set), and just need to find max len
        """
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest