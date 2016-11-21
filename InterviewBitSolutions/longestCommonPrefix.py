class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if len(A) == 0:
            return
        minLen = len(A[0])
        for str in A[1:]:
            if len(str) < minLen:
                minLen = len(str)

        for i in range(minLen):
            currentChar = A[0][i]
            for currentString in A[1:]:
                if currentString[i] != currentChar:
                    return currentString[:i]
        return A[0][:i+1]

sol = Solution()
A = [ "abcd", "abcde"]
print sol.longestCommonPrefix(A)


