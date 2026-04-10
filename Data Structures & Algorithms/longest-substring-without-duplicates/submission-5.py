class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        i str s
        o int longest substr no duplicate
        c s.len in [0, 1000]; ascii char
        e
        to find the longest substr,
        1. we start from left to check every char
        2. we store the index of every chr in a map

        if we find duplicate, we know the index of it's last show
        the l[index] should be the greater bewteen map[curr] + 1 and l
        if it's smaller than l, we need ignore for its out of window
        then we update char in the map

        if no duplicate, we just add the char to map

        now the new length is r - l + 1, compare with old max

        """
        
        l = 0
        freq = {}
        maxLen = 0

        for r in range(len(s)):
            if s[r] in freq:
                l = max(freq[s[r]] + 1, l)
            freq[s[r]] = r
            maxLen = max(maxLen, r - l + 1)

        return maxLen    
            
            


        