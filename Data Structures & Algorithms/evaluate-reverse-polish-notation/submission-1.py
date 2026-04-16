class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        operators = "+-*/"

        for i in tokens:
            if i in operators:
                topElement, secondTopElement = stack.pop(), stack.pop()
                if i == "+":
                    stack.append(secondTopElement + topElement)
                elif i == "-":
                    stack.append(secondTopElement - topElement)
                elif i == "*":
                    stack.append(secondTopElement * topElement)
                elif i == "/":
                    stack.append(int(secondTopElement/topElement))
            else:
                stack.append(int(i))
        return stack[-1]
        