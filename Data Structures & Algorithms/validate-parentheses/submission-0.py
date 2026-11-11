class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {"(": ")", "[": "]","{": "}"}

        for c in s: 
            if c in openToClose:
                stack.append(c)
            else:
                if not stack or openToClose[stack[-1]] != c: 
                    return False 
                stack.pop()
        return not stack 
            