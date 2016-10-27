class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        sum = 0
        for i in A:
            for j in A:
                if i == j:
                    continue
                cnt = 0
                bini = bin(i)[2:]
                binj = bin(j)[2:]
                lenDiff = max(len(bini), len(binj)) -  min(len(bini), len(binj))
                if len(bini) < len(binj):
                    bini = '0' * lenDiff + bini
                elif len(binj) < len(bini):
                    binj = '0' * lenDiff + binj
                for k in range(len(bini)):
                    if bini[k] != binj[k]:
                        cnt = cnt + 1
                if cnt < A:
                    sum += cnt
        return sum

sol = Solution()
A = [1,3,5]
print sol.cntBits(A)

A =[82, 2]
print sol.cntBits(A)
