class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        while B:

            A, B = B, A%B
            print A, B
        return A

sol = Solution()
print sol.gcd(8,12)
