import sys

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def wave(self, A):
        A = sorted(A)
        for i in range(0, len(A), 2):
            print i
            if i+1 < len(A) and A[i] < A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
        return A


sol = Solution()
print sol.wave([ 6, 17, 15, 13 ])
