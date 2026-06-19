class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                if not stack:
                    return False
                popped = stack.pop()
                if popped != mapping[char]:
                    return  False
            else:
                stack.append(char)
        return stack == []

        
