class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        list_partial = []
        for i, stra in enumerate(A[::-1]):
            result = ''
            carry = 0
            a = int(stra)
            for b in B[::-1]:
                b = int(b)
                m = (a*b) + carry
                print m
                if m > 9:
                    carry = m/10
                else:
                    carry = 0
                result = str(m)[-1] + result
            if(carry>0):
                result = str(carry)+ result
            print 'here', a,b, 'result', result, carry, m, str(m)[-1]
            list_partial.append(result)
        return list_partial
        #TODO: need to add elelments in list_partial
        result = ''
        for i, num in enumerate(list_partial):
            print i, num
            j = i + 1
            carry = 0
            k =0
            while True:
                sum_digits_at_i = str(carry)
                k += 1



        # for i range(len(list_partial)):


sol = Solution()
A = [ "222", "80"]
print sol.multiply(A[1], A[0])
