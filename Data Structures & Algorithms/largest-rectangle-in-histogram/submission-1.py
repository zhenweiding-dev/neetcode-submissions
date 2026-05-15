class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        i heights: [int], i is height a bar, width is 1
        o largest rectangle
        c 
        e
        for each bar, it self as the max height
        and reachs the max width when a smaller height shows up

        if a smaller height shows up, the smaller height's max width
        could start with larger ones before it

        so, we can use a stack to update the height and index
        when new smaller shows up, pop bigger ones and assign index to
        new smaller one
        """
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i # new bar's default width starts
            while stack and h < stack[-1][1]:
                # if smaller
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                # extend width
                start = index
            stack.append((start, h))
        
        # for bars not being poped
        for start, h in stack:
            max_area = max(max_area, h * (len(heights) - start))
        return max_area

