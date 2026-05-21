class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        i  matrix m*n; target
        o if target exist
        c non-decreasing order
        e
        the matrix can be treated as an orderd list
        r, c = divmod(i, n) 
        """
        m, n = len(matrix), len(matrix[0])
        length = m * n
        l, r = 0, length - 1
        while l <= r:
            mid = (l + r) // 2
            mr, mc = divmod(mid, n)
            if target < matrix[mr][mc]:
                r = mid - 1
            elif target > matrix[mr][mc]:
                l = mid + 1
            else:
                return True
        return False