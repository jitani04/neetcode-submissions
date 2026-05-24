class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = deque()
        pairs = {')': '(', ']': '[', '}': '{'}      
        for i in range(len(s)):
            if s[i] in pairs.values():
                stack.append(s[i])
            elif s[i] in pairs.keys() and stack and stack[-1] == pairs[s[i]]:
                stack.pop()
            else:
                return False 
        if not stack:
            return True
        else:
            return False
        

        