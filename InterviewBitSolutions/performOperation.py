def performOperation(op, operand1, operand2):
    # print op, operand1, operand2

    if op == '+':
        return operand1 + operand2
    if op == '-':
        return operand2 - operand1
    if op == '*':
        return operand1 * operand2
    if op == '/':
        try:
            return operand2 / operand1
        except ZeroDivisionError:
            #print 'Division by zero'
            return 0



class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        operators = {'+':'', '-':'', '*':'', '/':''}
        for op in A:
            if op in operators:
                if len(stack) < 2:
                    #print 'Error, not a valid list'
                    return
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(str(performOperation(op, int(operand1), int(operand2))))
            else:
                stack.append(op)
        return stack.pop()

sol = Solution()
A = ['2', '2', '/']
print sol.evalRPN(A)
