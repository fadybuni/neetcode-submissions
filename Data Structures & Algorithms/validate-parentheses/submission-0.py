class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(',']':'[','}':'{'}
        stack = []

        for i in s:
            if i in pairs:
                if stack and pairs[i] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else: 
                stack.append(i)
            
        if not stack:
            return True
        else:
            return False


        