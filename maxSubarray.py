def  maxLength(a, k):
    sum = 0
    maxSubArrayLength = 0
    for i, n in enumerate(a):
        sum = n
        currentLongest = 1
        for nextNum in a[i+1:]:
            if sum + nextNum <= k:
                sum += nextNum
                currentLongest += 1
            else:
                break
        maxSubArrayLength = max(currentLongest, maxSubArrayLength)
    return maxSubArrayLength

A = [74, 659, 931, 273, 545, 879, 924, 710, 441, 166, 493, 43, 988, 504, 328, 730, 841, 613, 304, 170, 710, 158, 561, 934, 100, 279, 817, 336, 98, 827, 513, 268, 811, 634, 980, 150, 580, 822, 968, 673, 394, 337, 486, 746, 229, 92, 195, 358, 2, 154, 709, 945, 669, 491, 125, 197, 531, 904, 723, 667, 550]
k = 22337
print maxLength(A, k)
