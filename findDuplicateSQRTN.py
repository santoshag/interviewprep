import math

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        sqrtLen = int(math.floor(math.sqrt(len(A))))
        lookup = [0] * sqrtLen
        print lookup
        container = -1
        for n in A:
            index = int(math.floor(n/sqrtLen))
            print n, index
            lookup[index] += 1
            if lookup[index] > sqrtLen:
                container = index
        d = {}
        if container == -1:
            return -1
        for n in A:
            index = int(math.ceil(n/sqrtLen))
            if index == container:
                if n in d:
                    return n
                else:
                    d[n] = 1
        return -2
        

                


sol = Solution()
A = [3, 4, 1, 4 ,1]
print sol.repeatedNumber(A)