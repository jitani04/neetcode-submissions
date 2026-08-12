class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {"}" : "{", "]" : "[", ")" : "("}
        # { key1 : value1, key2 : value2 }
        # access values with matches.values() access keys with 
        # matches.keys(), there is also matches.items()
        if len(s) == 1:
            return False
        for c in s:
            if c in matches:
                if stack and stack[-1] == matches[c]:
                    stack.pop()
                else: return False
            else:
                stack.append(c)
        if stack:
            return False
        return True

        