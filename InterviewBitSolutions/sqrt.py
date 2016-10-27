import sys

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A
        start = 1
        end = A
        ans = 0
        while start<=end:
            mid = (start+end)/2
            # print mid
            x = mid*mid
            if x == A:
                return mid
            if x < A:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans


sol = Solution()
print sol.sqrt(int(sys.argv[1]))
