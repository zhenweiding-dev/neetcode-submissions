from _heapq import heapify
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        i nums: [int]; k: int
        o lst[max ele in every window]
        c len(nums) in [1,100000], nums[i] in [-10000, 10000], k in [1, len(nums)]
        e len(nums) == 1: [nums[0]]; k == 1: nums
        """
        if k == 1:
            return nums
        
        output = []
        q = deque() # store index
        l = r = 0

        while r < len(nums):
            """
            as we need max value in the deque, if new is greater than left,
            the left can never be the max in the fllowing window,
            just drop it,
            by this, the left most (if exists) is greater than all its right
            that's the max-value(nums[q[0]])
            """
            while q and nums[q[-1]] <= nums[r]:
                q.pop()

            # add new element
            q.append(r)

            # check window size
            if l > q[0]:
                q.popleft()
            
            # append new result if window size reach k
            if (r - l + 1) >= k:
                output.append(nums[q[0]])
                # only window size has reached k, update l
                l += 1
            # update r
            r += 1
        return output


        


