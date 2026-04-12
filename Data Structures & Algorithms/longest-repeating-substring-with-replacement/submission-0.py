class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        i str s & int k, can change k char in s
        o longest substring with same char
        c len(s) in [1, 1000] k [0, len(s)] 
        e
        we can use sliding window, check chars in the window
        if r-l+1 - same chars < k
        it can grow
        else l += 1
        untill reach the end
        """
        freq = defaultdict(int)
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            curr = s[r]
            freq[curr] += 1
            maxf = max(maxf, freq[curr])
            while (r - l  + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
                
        return res
                
        