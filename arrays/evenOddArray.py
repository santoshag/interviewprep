def evenOddArray(A):
  nextEven = 0
  nextOdd = len(A)-1
  while nextEven < nextOdd:
    if A[nextEven]%2 == 0:
      nextEven += 1
    else:
      temp = A[nextEven]
      A[nextEven] = A[nextOdd]
      A[nextOdd] = temp
      nextOdd -= 1

A = [0,-2, -3, 1,3,4,5,6,7,8,9]
evenOddArray(A)
print A


