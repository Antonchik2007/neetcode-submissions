class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openPar = ["(", "[", "{"]
        closePar = [")", "]", "}"]
        #hashmap O(1) lookup
        convert = { 
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        #first par has to be open, and string has to be even to return True
        if s[0] not in openPar or len(s)%2 != 0:
            return False
        if len(s) == 0:
            return True
        for char in s:
            if char in openPar:
                stack.append(char)
            elif char in closePar and stack != []:
                if convert[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: 
                return False 
        if(stack):
            return False
        else:
            return True