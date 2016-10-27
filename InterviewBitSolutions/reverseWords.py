class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        result_list = []
        A = A.strip()
        word = ''
        addedToList = False

        for i, char in enumerate(A) :
          if char.isspace():
            if not addedToList:
              result_list.insert(0, word)
              addedToList = True
          else:
            if addedToList:
              word = ''
              addedToList = False
            word = word + char
        if A != "" and i == len(A) -1 and not char.isspace():
          result_list.insert(0, word)
        return ' '.join(result_list)
'''
ALTERNATE SOLUTION
def reverseWords(self, A):
        A = A.strip()
        A = A.split()
        A = A[::-1]
        return ' '.join(A)
'''


sol = Solution()
print "---" + sol.reverseWords("the           ") + "---"
