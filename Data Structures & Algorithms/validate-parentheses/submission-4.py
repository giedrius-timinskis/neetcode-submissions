class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposites = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in ['{', '[', '(']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                
                openingBracket = stack.pop()
                if openingBracket != opposites[c]:
                    return False

        return not len(stack)

        