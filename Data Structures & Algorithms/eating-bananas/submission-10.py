import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        i piles:[int] bannans in pile; h hours given
        o min k eat per hour; pile less than k have to stop and wait for next hour
        c len(piles) [1, 1000] <= h
        e 
        as len(piles) <= h, max_k = max(piles), eat max each always can finish
        min_k = 1
        use binary search looking for the smallest k between them
        """
        min_k, max_k = 1, max(piles)
        k = max_k
        while min_k <= max_k:
            mid_k = (min_k + max_k) // 2 
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / mid_k)
            if total_time <= h:
                k = mid_k
                max_k = mid_k - 1
            else:
                min_k = mid_k + 1
        return k




