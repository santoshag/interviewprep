def reqPainters(A, mid):
    total = 0
    numPainters = 1
    #print mid, A
    for i in range(len(A)):
        total += A[i]
        #print 'total', total
        if (total > mid):
            #print 'adding', A[i]
            total = A[i]
            numPainters += 1
    return numPainters

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        lo = max(C)
        hi = sum(C)
        n = len(C)
        # #print lo, hi, n
        while lo < hi:
            mid = lo+(hi-lo)/2
            #print lo, mid, hi
            requiredPainters = reqPainters(C, mid)
            #print mid, requiredPainters
            if requiredPainters <= A:
                hi = mid
            else:
                lo = mid + 1
        #print B, lo
        return B*lo

sol = Solution()
print sol.paint(2, 1, [12, 34, 67, 90])
