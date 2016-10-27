import math
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        count = n-1
        for i in range(count):
            # print range(i, count-i)
            for j in range(i, i + count):
                print n, i, j, A[i][j], A[n-1-j][i], A[n-1-i][n-1-j], A[j][n-1-i]
                temp = A[i][j]
                A[i][j] = A[n-1-j][i]
                A[n-1-j][i] = A[n-1-i][n-1-j]
                A[n-1-i][n-1-j] = A[j][n-1-i]
                A[j][n-1-i] = temp
            count -= 2
        return A


sol = Solution()
A = [[1, 2], [3,4]]
print sol.rotate(A)
print '[3 1 ] [4 2 ] \n\n'


A = [[1, 2,3], [4,5,6],[7,8,9]]
print sol.rotate(A)
print '[7 4 1 ] [8 5 2 ] [9 6 3 ]'

A = [[31, 32, 228, 333],  [79, 197, 241, 246],  [77, 84, 126, 337],  [110, 291, 356, 371]]
print sol.rotate(A)
print '[110 77 79 31 ] [291 84 197 32 ] [356 126 241 228 ] [371 337 246 333 ]\n\n'


