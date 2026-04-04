class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = list(s), list(t)
        a.sort()
        b.sort()
        return a == b