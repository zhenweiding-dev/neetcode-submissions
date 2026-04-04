class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        i list of strs
        o list of list(group of anagrams strs or alone str)
        c only lowercase
        e empty or one element; 
        """
        # case 1: no element or just one element
        if len(strs) <= 1:
            return [strs]
        
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # convert to tuple as dict keys and keys must be immutable
            res[tuple(count)].append(s)
        
        return list(res.values())