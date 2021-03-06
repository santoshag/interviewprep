import sys
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
      l = 0
      h = len(A) -1
      rotated = True
      while l<=h:
        rotated = False
        m = (l+h)/2
        if A[m] == B:
          return m
        if A[l] > A[h] or A[m] > A[h]:
          rotated = True
        if not rotated and A[m] < B:
          l = m + 1
        elif not rotated and A[m] > B:
          h = m -1
        # print A[l], A[m], A[h],
        elif rotated and (B > A[m] and B > A[l] and B <= A[h]) or ( B > A[m] and B <= A[h]) or (B < A[l] and B <= A[h]):
          # print 'search right'
          l = m+1
        else:
          # print 'search left'
          h = m-1
      return m-1


sol = Solution()
A = [ 180, 181, 182, 183, 184, 187, 188, 189, 191, 192, 193, 194, 195, 196, 201, 202, 203, 204, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16, 17, 18, 19, 23, 26, 27, 28, 29, 32, 33, 36, 37, 38, 39, 41, 42, 43, 45, 48, 51, 52, 53, 54, 56, 62, 63, 64, 67, 69, 72, 73, 75, 77, 78, 79, 83, 85, 87, 90, 91, 92, 93, 96, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 111, 113, 115, 116, 118, 119, 120, 122, 123, 124, 126, 127, 129, 130, 135, 137, 138, 139, 143, 144, 145, 147, 149, 152, 155, 156, 160, 162, 163, 164, 166, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177 ]
for i in A:
  print sol.search(A, i)
