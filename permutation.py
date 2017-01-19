count = 0

def permutation(A):
    permute(A, 0, len(A))

def permute(A, start, end):
    global count
    if start == end:
        count += 1
        print count, "".join(A) #you can use pretty print  abstract method in an interview
        return 
    for i in range(start, end):
        A[start], A[i] = A[i], A[start] #use swap abstract method 
        permute(A, start+1, end)
        A[start], A[i] = A[i], A[start]

permutation(['a', 'b', 'c', 'd'])