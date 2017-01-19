class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(A):
        currentMax = 0
        for i in range(len(A)):
            maxPalinLength = checkPalindrome(A, i, i)
            if maxPalinLength > currentMax:
                currentMax = maxPalinLength

            if i+1 < len(A):
                maxPalinLength = checkPalindrome(A, i, i+1)
                if maxPalinLength > currentMax:
                    currentMax = maxPalinLength

        return currentMax

        if currentMax > 0:
            return (currentMax, maxStartIndex, maxEndIndex)
        else:
            return

    def checkPalindrome(A, head, tail):
        palinLength = 0
        while head >= 0 and tail <= len(A) - 1:
            if A[head] != A[tail]:
                return (head+1, tail-1)
            else:
                head -= 1
                tail += 1
        return tail - head



sol = Solution()
A = "ab"
palinLength, head, tail = sol.longestPalindrome(A)
print A[head:tail+1], palinLength, head, tail

