class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0,len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[' :
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                ch = stack[-1]
                stack.pop()
                if (s[i] == ')' and ch == '(') or (s[i] == '}' and ch == '{') or (s[i] == ']' and ch == '['):
                    continue
                else : 
                    return False

        return len(stack) == 0 
            
            

        