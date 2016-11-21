def partitionDNF(A, p1, p2, p3, p4):
    k1, k2 = 0, 0
    k3, k4 = len(A) - 1, len(A) - 1
    counter = 1
    while k2 <= k3:
        print k1, k2, k3, k4, A[k2], A, counter
        counter += 1
        if A[k2] == p1:
            A[k1], A[k2] = A[k2], A[k1]
            # No need to check if k1 < k2 as it A[k1] is guaranteed to p2.
            k2 += 1
            k1 += 1
        elif A[k2] == p2:
            k2 += 1
        elif A[k2] == p3:
            A[k2], A[k3] = A[k3], A[k2]
            k3 -= 1
        elif A[k2] == p4:
            if k3 < k4:
                A[k3], A[k4] = A[k4], A[k3]
                k3 -= 1
            A[k4], A[k2] = A[k2], A[k4]
            k4 -= 1


A = [1, 2, 3, 4, 1, 2, 3, 4]
p1, p2, p3, p4 = 1, 2, 3, 4
print 'Before partition:', A, p1, p2, p3, p4
partitionDNF(A, p1, p2, p3, p4)
print 'After partition:', A
