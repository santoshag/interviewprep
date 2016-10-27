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
            str = A[0]
            for j, nextStr in enumerate(A[1:]):
                # print str[i], nextStr[i]
                if nextStr[i] != str[i]:
                    return str[0:i]
                str = nextStr
        return str[:i+1]

sol = Solution()
A = [ "abcd", "abcde"]
print sol.longestCommonPrefix(A)


