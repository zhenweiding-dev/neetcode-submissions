class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_T, count_S = {}, {}

        for i in range(len(s)):
            count_S[s[i]] = 1 + count_S.get(s[i], 0)
            count_T[t[i]] = 1 + count_T.get(t[i], 0)
        
        return count_S == count_T
