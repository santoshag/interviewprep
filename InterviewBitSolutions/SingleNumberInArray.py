class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        if len(A) == 0:
            return
        if len(A) == 1:
            return A[0]
        res = A[0]
        for i in range(1, len(A)):
            res = res ^ A[i]
        return res

sol = Solution()
A = [1,1,2,2,3]
print sol.singleNumber(A)
