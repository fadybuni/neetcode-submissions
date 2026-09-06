import operator
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+": operator.add, "-":operator.sub, "*":operator.mul, "/":lambda a,b: int(a/b)}

        stack = []
        res = None
        for token in tokens:
            if token.lstrip("-").isalnum():
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(op[token](a,b))
        return stack[-1]

