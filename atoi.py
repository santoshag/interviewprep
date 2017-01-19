# Complete the function below.


def  atoi(str):
    if str is None:
        return 0
    resultStr = ''
    i = 0
    while str[i].isspace():
        i += 1
    if str[i] == '+' or str[i] == '-' and i+1 < len(str) and str[i+1].isdigit():
        resultStr = resultStr + str[i]
    else:
        return 0
    i = i + 1
    while i < len(str) and str[i].isdigit():
        resultStr = resultStr + str[i]
        i += 1
    print resultStr
    return int(resultStr)


print atoi("c++")