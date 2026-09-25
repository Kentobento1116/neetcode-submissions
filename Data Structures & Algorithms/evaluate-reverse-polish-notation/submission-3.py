class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            if element == '+':
                stack.append(stack.pop() + stack.pop())
            elif element == '-':
                op2, op1 = stack.pop(), stack.pop()
                stack.append(op1 - op2)
            elif element == '*':
                stack.append(stack.pop() * stack.pop())
            elif element == '/':
                op2, op1 = stack.pop(), stack.pop()
                stack.append(int(float(op1 / op2)))
            else:
                stack.append(int(element))
        return stack[0]