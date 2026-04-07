class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        i lst of int sorted incre
        o [index1, index2] sum=target
        c index1 < index2; only one solution; o(1)space
        e
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i + 1, j + 1]
            
                