class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        base = 0
        length = len(A)
        newLength = len(A)
        for nextNum in A[1:]:
            print A[base], nextNum, A
            if A[base] == nextNum:
                newLength -= 1
            else:
                base += 1
                A[base] = nextNum
        for i in range(newLength, length):
            # print i
            A[i] = 0
        # print A, newLength
        return newLength

sol = Solution()
A = [2,3,5,5,13,13]
print 'New length is', sol.removeDuplicates(A)
print 'Array: ', A

