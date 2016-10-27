import sys

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A < 1:
            return []
        r = [[1]]
        for i in range(1, A):
            row = []
            for j in range(0, i+1):
                if j-1 < 0:
                    row.append(r[i-1][j])
                elif j > i-1:
                    row.append(r[i-1][j-1])
                else:
                    row.append(r[i-1][j] + r[i-1][j-1])
            r.append(row)
        return r


sol = Solution()
print sol.generate(int(sys.argv[1]))
