def partitionDNF(A, pivot):
    smaller,equal = 0, 0
    larger = len(A) -1
    while equal < larger:
        print smaller, equal, larger, A[equal]
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            A[larger], A[equal] = A[equal], A[larger]
            larger -= 1

A = [4, 5, 6, 5, 6, 6,7,8,8, 9,10,9,10,1,3]
pivot = 10
print 'Before partition:', A, 'Pivot:', pivot
partitionDNF(A, pivot)
print 'After partition:', A