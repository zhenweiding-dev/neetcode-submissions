class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # use {key:[str, ]} to store result

        for i in strs:
            count = [0] * 26
            for k in i:
                count[ord(k) - ord('a')] += 1
            res[tuple(count)].append(i)
        return list(res.values())