dimport sys
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        if A <= 0:
            return
        mat=[]
        for i in range(2*A -1):
            col = [0] * (2*A -1)
            mat.append(col)
        T = 0
        L = 0
        R = 2*A-2
        B = 2*A-2
        n = A
        dir = 0
        while T <= B and L <= R:
            if dir == 0:
                for i in range(L, R+1):
                    mat[T][i] = n
                T += 1
                dir = 1
            elif dir == 1:
                for i in range(T, B+1):
                    mat[i][R] = n
                R -= 1
                dir = 2
            elif dir == 2:
                for i in range(R, L-1, -1):
                    mat[B][i] = n
                B -= 1
                dir = 3
            elif dir == 3:
                for i in range(B, T-1, -1):
                    mat[i][L] = n
                L += 1
                dir = 0
                n -= 1
        return mat

sol = Solution()
mat = sol.prettyPrint(int(sys.argv[1]))
for i in range(len(mat)):
    print mat[i]

