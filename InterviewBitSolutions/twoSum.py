def op(B, n):
  return B - n

class Solution:

    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        d = {A[0]:1}
        for i, n in enumerate(A[1:]):
            val = B - n
            if val in d:
                # print d, B-n, d[B-n], n ,i
                return sorted([d[val], i+2])
            elif n not in d:
                # print 'adding', n, i+2
                d[n] = i+2
        return []

sol = Solution()
# A = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
A = [ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8]

for i, n in enumerate(A):
  print i+1, ":", A[i]
l = sol.twoSum(A, -1)
print l, A[l[0]], A[l[1]], A[l[0]]+ A[l[1]]
