def almost_palindromes(str):
    if str == None:
      return
    score = 0
    #check for only first half against second half
    for i in range(len(str)/2):
        if str[i] != str[len(str)-1-i]:
            score += 2
    return score

print almost_palindromes("abc")
