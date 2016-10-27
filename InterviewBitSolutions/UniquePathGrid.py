import math

def fact(n):
    return math.factorial(n)



class Solution:
    # @param A : list of integers
    # @return a list of integers
    def uniquePaths(self, m, n):
        if m==0 || n==0:
            return 0
        return fact(m+n-2)/(fact(n-1) * fact(m-1))

sol = Solution()
print sol.uniquePaths(0, 1)



