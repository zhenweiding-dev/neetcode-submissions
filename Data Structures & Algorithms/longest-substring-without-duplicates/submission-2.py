class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        i str s
        o int longest substr no duplicate
        c s.len in [0, 1000]; ascii char
        e
        """
        l = 0
        curr = set()
        maxLen = 0

        for r in s:
            while r in curr:
                curr.remove(s[l])
                l += 1
            else:
                curr.add(r)
                maxLen = max(maxLen, len(curr))
                
        return maxLen
            
            
            


        