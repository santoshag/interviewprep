import sys
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
      #find minimum's index
      low = 0
      high = len(A) -1
      lenA = len(A)
      while low <= high:
        mid = (low+high)/2
        if A[mid] >= A[high]:
          low = mid+1
        elif A[mid] <= A[high]:
          high = mid
      minIndex = low-1

      # print minIndex
      if B >= A[minIndex] and B <= A[lenA-1]:
        low = minIndex
        high = len(A)-1
      else:
        low = 0
        high = minIndex
      # print low, high
      while low<=high:
        mid = (low+high)/2
        if A[mid] == B:
          return mid
        if A[mid] < B:
          low = mid + 1
        else:
          high = mid -1
      return -1






sol = Solution()
A = [ 5,6,1,2,3,4]
for i in A:
  print sol.search(A, i)
