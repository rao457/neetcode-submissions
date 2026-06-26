class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = (total + 1) // 2

        low, high = 0, len(A)

        while (low <= high):
            cutA = (low + high) // 2
            cutB = half - cutA

            Aleft = float('-inf') if cutA == 0 else A[cutA - 1]
            Aright = float('inf') if cutA == len(A) else A[cutA]

            Bleft = float('-inf') if cutB == 0 else B[cutB - 1]
            Bright = float('inf') if cutB == len(B) else B[cutB]

            if Aleft <= Bright and Bleft <= Aright:
                if (total % 2 == 1):
                    return max(Aleft, Bleft)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                high = cutA - 1
            else:
                low = cutA + 1
            