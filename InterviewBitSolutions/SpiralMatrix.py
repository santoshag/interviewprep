class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []

        ## Actual code to populate result
        #t-top l-left b-bottom r-right pointers, dir-direction
        t = 0
        l = 0
        b = len(A) -1
        r = len(A[0]) - 1
        dir = 0
        result = []
        while t<= b and l <= r:
            # print t, r, b, l, dir
            if dir == 0:
                for i in range(l, r+1):
                    # print t, i
                    result.append(A[t][i])
                t += 1
                dir = 1
            elif dir == 1:
                for i in range(t, b+1):
                    result.append(A[i][r])
                r -= 1
                dir = 2
            elif dir == 2:
                for i in range(r, l-1, -1):
                    # print i, b, l, dir
                    result.append(A[b][i])
                b -= 1
                dir = 3
            elif dir == 3:
                for i in range(b, t-1, -1):
                    result.append(A[i][l])
                l += 1
                dir = 0
        return result

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
sol = Solution()
print sol.spiralOrder(A)
