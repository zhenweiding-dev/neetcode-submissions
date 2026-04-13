class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        i strs s1 s2
        o T if s2 contains a permutation of s1
        c len(s1) >= 1, len(s2) <= 1000
        e len(s1) > len(s2) F
        use len(s1) as fixed window length
        check s2 with sliding window
        also can use asii to save memory
        """
        if len(s1) > len(s2):
            return False
        
        s1Count, windowCount = [0] * 26, [0] * 26

        windowSize = len(s1)

        for i in range(windowSize):
            s1Count[ord(s1[i]) - ord('a')] += 1
            windowCount[ord(s2[i]) - ord('a')] += 1
        
        for r in range(windowSize, len(s2)):
            if s1Count == windowCount:
                return True
            windowCount[ord(s2[r]) - ord('a')] += 1
            windowCount[ord(s2[r - windowSize]) - ord('a')] -= 1
        return s1Count == windowCount
        
            
             