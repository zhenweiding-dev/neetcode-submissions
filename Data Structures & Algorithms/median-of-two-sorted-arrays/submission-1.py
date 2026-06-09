class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        as they are sorted, we can cut at some position
        and only make sure left have half elements
        and we can choose the smaller array as base
        and caulate the cut position at another array
        and check if left in both part is less than right part
        """
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2 # half = i + j + 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")

            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # we cut at i, j. as they are sorted.
            # we only need to check nums1[i] with nums2[j+1]
            # and nums2[j] with nums1[i+1] 
            if Aleft <= Bright and Bleft <= Aright:
                    if total % 2:
                        return min(Aright, Bright) # needs i+1/j+1
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright: # i is too big, take it as boundary
                r = i - 1
            else: # i is too small
                l = i + 1
