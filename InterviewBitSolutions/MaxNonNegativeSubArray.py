import sys

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def maxset(self, A):
        max_sum = 0
        max_list = []
        current_sum = 0
        current_list = []
        loop = 0
        for i, num in enumerate(A):
            print loop, num, current_sum, current_list, max_sum, max_list
            if num >= 0:
                loop = 1
                #positive num
                current_list.append(num)
                current_sum += num
            if (num < 0 and current_sum >= max_sum) or i == len(A)-1:
                loop = 2
                if num >= 0:
                    if current_sum > max_sum:
                        max_list = current_list
                        max_sum = current_sum
                    elif len(max_list) < len(current_list):
                        max_list = current_list
                        max_sum = current_sum
                #negetive num
                elif current_sum > max_sum:
                    max_list = current_list
                    max_sum = current_sum
                elif len(max_list) < len(current_list):
                    max_list = current_list
                    max_sum = current_sum
                #else len(max_list) == len(current_list) : dont change the max_list
            if num < 0:
                current_sum = 0
                current_list = []

            loop = 0
        return max_list

sol = Solution()
A = [ 24115, -75629, -46517, 30105, 19451, -82188, 99505, 6752, -36716, 54438, -51501, 83871, 11137, -53177, 22294, -21609, -59745, 53635, -98142, 27968, -260, 41594, 16395, 19113, 71006, -97942, 42082, -30767, 85695, -73671 ]
print A
print sol.maxset(A)
