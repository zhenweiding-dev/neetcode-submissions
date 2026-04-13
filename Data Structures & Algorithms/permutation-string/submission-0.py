from collections import Counter
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
        
        freqS1 = Counter(s1)
        l = 0
        freqWin = defaultdict(int)

        for r in range(len(s2)):
            freqWin[s2[r]] += 1

            if r - l + 1 > len(s1):
                if freqWin[s2[l]] == 1:
                    del freqWin[s2[l]]
                else:
                    freqWin[s2[l]] -= 1
                l += 1

            if freqWin == freqS1:
                return True
    
        return False
            
             