class Solution:
    # @param A : tuple of integers
    # @return a tuple with (start_inedx, end_index, max_sum)
    def maxSubArraySum(self, A):
        if len(A) == 0:
            return
        max_sum = current_sum = A[0]
        start_index = end_index = 0
        for i, num in enumerate(A[1:]):
            # print i+1 , num
            if num >= current_sum+num:
                start_index = i + 1
                end_index = i + 1
            current_sum = max(current_sum+num, num)
            if current_sum > max_sum:
                #if choosing a new max_sum, record end_index here
                end_index = i + 1
            max_sum = max(max_sum, current_sum)
        return (start_index, end_index, max_sum)

sol = Solution()
A = [ 1000, -1100, 200, 300, 700, -1200]
print sol.maxSubArraySum(A)
A = [ -2,1,-3,4,-1,2,1,-5,4]
print sol.maxSubArraySum(A)
print '[7 4 1 ] [8 5 2 ] [9 6 3 ]'
