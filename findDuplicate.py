def getDuplicate(A):
  for n in A:
    getActualValue(n)
    if A[n] < 0:
      return n
    if A[n] == 0:
      A[0] = -n
    else:
      A[n] = -A[n]
  return -1
