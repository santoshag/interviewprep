class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        base = 0
        length = len(A)
        newLenght = len(A)
        for nextNum in A[1:]:
            # print A[base], nextNum, A
            if A[base] == nextNum:
                newLenght -= 1
                continue
            else:
                base += 1
                A[base] = nextNum
        # print A, newLenght
        return newLenght

sol = Solution()
print sol.removeDuplicates([5000,5000,5000])
