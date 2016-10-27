


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        r = []
        carry = 1
        k = 0
        for i in range(len(A)-1, -1, -1):
            if len(A) > k:
                l = A[i] + carry
            else:
                l = carry
            carry = l / 10
            l = l % 10
            r.insert(0, l)
        if carry>0:
            r.insert(0, carry)
        num_of_zeros = 0
        for i in range(len(r)):
            if r[i] > 0:
                break
            else:
                num_of_zeros += 1

        result = r[num_of_zeros:]
        return result


sol = Solution()
print sol.plusOne([ 0, 0, 4, 4, 6, 0, 9, 6, 5, 1 ])



