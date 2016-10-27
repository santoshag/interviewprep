import math
def processLine(line, B):
    char_lenght = 0
    for word in line:
        char_lenght += len(word)
    if len(line) > 1:
        spaces = math.ceil((B - char_lenght)/(len(line)-1))
    else:
        spaces = B - char_lenght
    processLine=''
    for word in line[:-1]:
        print word
        processLine += word+ ('*' * int(spaces))
    processLine = processLine + line[-1]
    print processLine, len(processLine)

class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        lines = []
        line = []
        line_lenght = 0
        for i, str in enumerate(A):
            if str == 'justification.':
                isPrint = True
            word_count_in_line = len(line) + 1
            if word_count_in_line <= 1:
                spaces = 0
            else:
                spaces = word_count_in_line -1
            if line_lenght+len(str) + spaces <= B:
                line.append(str)
                line_lenght += len(str)
            else:
                lines.append(line)
                line = []
                line.append(str)
                line_lenght = len(str)
        if line_lenght < B and i == len(A)-1:
            lines.append(line)
        result = []
        for line in lines:
            print line
            result.append(processLine(line, B))


sol = Solution()
A = ["This", "is", "an", "example", "of", "text", "justification."]
print sol.fullJustify(A, 16)
