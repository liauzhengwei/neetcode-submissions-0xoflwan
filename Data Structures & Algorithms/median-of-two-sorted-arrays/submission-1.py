class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(A) > len(B):
            A,B = B,A

        m,n = len(A), len(B)
        left, right = 0, m

        while left <= right:
            i = (left + right) //2
            j = (m + n + 1)//2 - i

            maxLeftA = A[i-1] if i>0 else float('-inf')
            minRightA = A[i] if i<m else float('inf')

            maxLeftB = B[j-1] if j>0 else float('-inf')
            minRightB = B[j] if j<n else float('inf')

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 1:
                    return max(maxLeftA, maxLeftB)
                else:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) /2
            elif maxLeftA > minRightB:
                right = i - 1
            else:
                left = i + 1