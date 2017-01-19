def printAll(arr, i):
  if i == len(arr) -1:
    print arr[:]
    return
  for j in range(len(arr)):
    swap(arr, arr[i], arr[j])
    printAll(arr, i+1)
    swap(arr, arr[i], arr[j])
