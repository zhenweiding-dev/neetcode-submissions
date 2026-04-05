class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        i list of nums, int k
        o k most freq of the elements in the list
        c answer is unique(no similar freq count > k); distinct elements >= k >= 1
        e 
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res        
