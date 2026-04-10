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
        3. when we find duplicate, we know the index of it's last show
        4. so the curr length is curr[index] - l[index]
        5. new start is the map[curr] + 1
        """
        
        l = 0
        freq = defaultdict(int)
        maxLen = 0

        for r in range(len(s)):
            if s[r] in freq.keys():
                l = max(freq[s[r]] + 1, l)
            freq[s[r]] = r
            maxLen = max(maxLen, r - l + 1)

        return maxLen    


            
            
            


        