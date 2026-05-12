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
       to track the index, we can use tuple in the stack
        """
        length = len(temperatures)
        if length == 1:
            return [0]
    
        stack = []
        res = [0] * length

        for i in range(length):
            temper = temperatures[i]
            if not stack or temper <= stack[-1][-1]:
                stack.append((i, temper))
            else:
                while stack and temper > stack[-1][-1]:
                    j, _ = stack.pop()
                    res[j] = i - j
                stack.append((i, temper))
        
        return res

        
