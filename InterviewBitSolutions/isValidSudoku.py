class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
      #check rows

      for i in range(9):
        d = {}
        for j in range(9):
          if A[i][j] == '.':
            continue
          num = int(A[i][j])
          if num > 9 or num < 1:
            return 0
          if num in d:
            return 0
          else:
            d[num] = 1

      #check columns
      for i in range(9):
        d = {}
        for j in range(9):
          if A[j][i] == '.':
            continue
          num = int(A[j][i])
          if num in d:
            return 0
          else:
            d[num] = 1
      #check blocks
      nc = 0
      count = 0
      for i in range(9):
        d = {}
        # print '\n'
        nb = (i * 3)
        for j in range(3):
          for k in range(3):
            num = A[(nb+j)%3 + count][k+nc]
            if num == '.':
              continue
            num = int(num)
            if num in d:
              return 0
            else:
              d[num] = 1
        nc = (nc+3)%9
        if i >= 5:
          count = 6
        elif i>=2:
          count = 3
      return 1

sol = Solution()
A = ["53..7....", "6..195...", ".99....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
print sol.isValidSudoku(A)
