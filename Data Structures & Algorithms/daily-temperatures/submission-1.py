class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        i temper[int], i repre ith tem
        o restult[int], result[i] means after i days, temp is higher than ith, if not exist, 0
        c len(temp) in [1, 1000]; temp[i] in [0, 100]
        e lenth is 1, just return[0]
        brute force(n^2)
        for the first, need to compare all until find larger
        seems we can use a stack,
        if push first, if next if larger, pop and push
        if next is smaller, push, compare next's next
        if larger, pop and compare, if still larger, pop and compare
        if smaller, push
       as we also need to track the index, we can just store the index
        """
        length = len(temperatures)

        stack = []
        res = [0] * length

        for i, temper in enumerate(temperatures):

            while stack and temper > temperatures[stack[-1]]:
                    j = stack.pop()
                    res[j] = i - j

            stack.append(i)
                
        return res

        
