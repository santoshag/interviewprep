import sys

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def getRow(self, k):
        if k < 0:
            return []
        k = k + 1
        current_row = [1]
        if k == 1:
            return current_row
        for i in range(2, k+1):
            row = [1] * i
            row[0] = 1
            row[i-1] = 1
            for j in range(1, i-1):
                row[j] = current_row[j-1] + current_row[j]
            current_row = row
        return current_row

sol = Solution()
print sol.getRow(int(sys.argv[1]))
