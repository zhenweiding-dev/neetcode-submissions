class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        i lst of nums
        o n: the length of longest consecutive seq
        c len in [0,1000]
        e length 0, 1
        for each sequence, we can take it as a node, each num only need to know
        the length from begin to it, and next just need to add one
        for num connect two node, need to add length together
        """
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1 #left length + right + 1
                mp[num - mp[num - 1]] = mp[num] #update head
                mp[num + mp[num + 1]] = mp[num] #undate trail
                res = max(res, mp[num])
        return res
            