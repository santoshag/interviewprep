def multiply(A, B):
    result = []
    resultPositive, A, B = isResultPositive(A, B)
    A = removeZerosAtStart(A)
    B = removeZerosAtStart(B)
    for i in range(len(B) - 1, -1, -1):
        partialProd = multiplyAwithBDigit(A, B[i], result)
        addPartialProdToResult(partialProd, result, len(B) - 1 - i)
    if not resultPositive:
        result.insert(0, '-')
    return result


def isResultPositive(A, B):
    aNegetive = False
    bNegetive = False
    returnVal = True
    if A[0] == '-':
        A = A[1:]
        aNegetive = True
    if B[0] == '-':
        B = B[1:]
        bNegetive = True
    if aNegetive ^ bNegetive:
        returnVal = False
    return (returnVal, A, B)


def multiplyAwithBDigit(A, bDigit, result):
    carry = 0
    partialProd = []
    for i in range(len(A) - 1, -1, -1):
        aDigit = A[i]
        prod = (aDigit * bDigit) + carry
        carry = prod / 10
        val = prod % 10
        partialProd.insert(0, val)
    if carry > 0:
        partialProd.insert(0, carry)
    return partialProd


def addPartialProdToResult(partialProd, result, startPos):
    carry = 0
    for i in range(len(partialProd) - 1, -1, -1):
        bdigit = partialProd[i]
        if len(result) - 1 - startPos >= 0 and len(result) - 1 - startPos < len(result):
            adigit = result[len(result) - 1 - startPos]
        else:
            adigit = 0
        sum = adigit + bdigit + carry
        carry = sum / 10
        val = sum % 10
        if len(result) - 1 - startPos >= 0 and len(result) - 1 - startPos < len(result):
            result[len(result) - 1 - startPos] = val
        else:
            result.insert(0, val)
        startPos += 1

    if carry > 0:
        result.insert(0, carry)


def removeZerosAtStart(result):
    zerosCount = 0
    for n in result:
        if n > 0:
            break
        zerosCount += 1
    return result[zerosCount:]


A = [0, 0, 1, 2, 3]
B = ['-', 0, 9, 0]
result = multiply(A, B)
print '* Result:', result
