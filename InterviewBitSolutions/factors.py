import math

class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        factors = []
        count = 0
        for i in range(1, int(math.sqrt(A))+1):
            if A%i == 0:
                factors.insert(count, i)
                if i!= math.sqrt(A):
                    factors.insert(len(factors) - count, A/i)
                count += 1
        return factors

sol = Solution()
print sol.allFactors(2)
