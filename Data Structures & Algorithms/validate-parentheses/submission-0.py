class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        matching = {')': '(', 
                    '}': '{', 
                    ']': '['
        }

        for char in s:
            if char in matching:
                if stack and stack[-1] == matching[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0   

