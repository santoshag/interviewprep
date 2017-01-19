def  isPalindrome(strarr):
    return isPalin(strarr, 0, len(strarr)-1)

def isPunct(char):
    return char == '.' or char == ',' or char == '!'or char == '-'or char == ';'or char == ':' or char == ''or char == '"' or char =='\n'
    
def isPalin(s, start, end):
    print s, start, end
    while start <end and isPunct(s[start]):
        start += 1
    while  start <end and isPunct(s[end]):
        end -= 1
    if start >= end:
        return True
    return s[start] == s[end] and isPalin(s, start+1, end-1)

print isPalindrome("test")