class Solution:
    # @param A : list of integer
    # @return a list of integer such that A[i] = A[k] * A[l] where 0 <= k,l < len(array) and k,l != i 
    def arrayProduct(self, A):
        product_before = 1
        product = []
        for n in A:
            product.append(product_before)
            product_before *= n
        product_after = 1
        for i,n in reversed(list(enumerate(A))):
            product[i] *= product_after
            product_after *= n
        return product

def main():
    n = int(raw_input())
    arr = []
    for i in range(0,n):
        num = int(raw_input())
        arr.append(num)
    
    #for testing in here
    arr = [1,2,3,4,5]
    solution = Solution()
    print solution.arrayProduct(arr)


if __name__ == "__main__":
    main()


